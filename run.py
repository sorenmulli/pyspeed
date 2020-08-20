#!/usr/bin/env python3
import os, sys
from argparse import ArgumentParser

from src.testfuncs import retrieve_functions, run_all_tests, report_results, save_results

if __name__ == '__main__':
	implementations = (
		'pure',
		'numpy',
		'torch_cpu',
		'cython_pure',
		'cython_c',
		'ctype_c',
		'ctype_rust',
	)
	cases = {
		'rootloop': [10**i for i in range(5, 7)],
	}

	parser = ArgumentParser(description="Test speed of Python implementations on a number of code cases")
	parser.add_argument('--impl',  type=str, nargs='+', help='What implementations to test. If not given, test all')
	parser.add_argument('--cases', type=str, nargs='+', help='What cases to test. If not given, test all')
	parser.add_argument('--reps',  type=int, help='Number of repetitions for each combination (default=10)', default=10)
	parser.add_argument('--out',   type=str, help='Folder to save results (default: working dir.)', default='')

	args = parser.parse_args()

	if args.impl: implementations = args.impl
	if args.cases: cases = {name: cases[name] for name in args.cases}

	all_funcs = retrieve_functions( implementations, cases.keys(), os.path.join(os.path.dirname( sys.argv[0] ), 'src') )

	print(f"Starting evaluation of {len(cases)} case(s) in {len(implementations)} different implementation(s).")
	print(f"Repetitions: {args.reps}. Function calls: {len(implementations) * args.reps * sum(len(c) for c in cases.values())} (each case may test multiple arguments)")
	print()

	all_results = run_all_tests(all_funcs, cases, args.reps)
	result_report = report_results(all_results, cases, args.reps)
	save_results(all_results, result_report, args.out)

	print(result_report)
	print()
	print(f"Results and report saved to {os.path.abspath(args.out)}.")
	print("Results are pickled as a dict of dicts with numpy ndarrays as values.")
