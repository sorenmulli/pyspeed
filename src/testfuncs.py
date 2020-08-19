import sys, os
import pickle
from importlib import import_module # import import as import
from time import perf_counter

import numpy as np

def take_time(func, *args) -> float:
	""" Time used for function evaluation in seconds (float)  """
	t = perf_counter()
	func(*args)
	return perf_counter() - t

def run_test(func, combinations: list, reps: int) -> np.ndarray:
	"""
	Evaluates `func` for each argument in combinations reps times.
	Gives results in array of shape (n_combinations, n_reps)
	"""
	return np.array([
		[ take_time(func, args) for args in combinations ] for _ in range(reps)
		])

def run_all_implementations(funcs: dict, comb: list, reps: int) -> dict:
	return { name: run_test(func, comb, reps) for (name, func) in funcs.items()  }

def run_all_tests(funcs: dict, cases: dict, reps: int) -> dict:
	return { case: run_all_implementations(funcs[case], combs, reps) for (case, combs) in cases.items() }

def report_results(results: dict, caseargs: dict, reps: int) -> str:
	""" Generates a string reporting the results (mean and stds.) of run times """
	lines = list()
	lines.append( f"Evaluation finished. Results: mean and std. over {reps} repetitions")
	lines.append("".join("-" for _ in range(70)))
	for casename, case_results in results.items():
		lines.append(f"\tCase: {casename}. Tested args: {caseargs[casename]}")
		lines.append("\t" + "".join("-" for _ in range(50)))
		for implname, impl_results in case_results.items():
			means, stds = impl_results.mean(0), impl_results.std(0)
			with np.printoptions(precision=2):
				lines.append(f"\t\t{implname}: {means}")
				lines.append(f"\t\t{' '*(len(implname)-3)}+/-: {stds}\n")
	return "\n".join(lines)

def save_results(all_results: dict, report: str, path: str):
	with open(os.path.join(path, 'results.dat' ), 'wb') as outfile:
		pickle.dump(all_results, outfile)
	with open(os.path.join(path, 'report.txt') , 'w') as outfile:
		outfile.write(report)

def retrieve_functions(implementations: dict, cases: list) -> dict:
	funcs = { name : dict() for name in cases }
	# sys.path.append( os.path.join( sys.argv[0], implementation ) )

	for implementation in implementations:
		mod = import_module( implementation )
		for fname in cases: funcs[fname][implementation] = getattr(mod, fname)

	return funcs
