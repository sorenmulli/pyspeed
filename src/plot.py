import os
import matplotlib.pyplot as plt
import numpy as np

rc_params = { "font.size": 20, "legend.fontsize": 18, "legend.framealpha": 0.8 }
plt.rcParams.update(rc_params)

os.makedirs("plots", exist_ok=True)

def make_plots(cases, all_results, system_info: str):
    assert cases.keys() == all_results.keys(), "Keys of cases and all_results must match"
    for (case, sizes), results in zip(cases.items(), all_results.values()):
        plt.figure(figsize=(15, 10))
        for i, (impl, runtimes) in enumerate(results.items()):
            lw = 5 - 3 * i / len(results)
            ls = ['--', '-.', ':'][i % 3]
            plt.plot(sizes, runtimes.mean(axis=0), linewidth=lw, linestyle=ls)
            plt.scatter(sizes, runtimes.mean(axis=0), s=40, label=impl)
        plt.title(f"Function {case}\n{system_info}")
        plt.xticks(sizes)
        plt.xlabel("Function input")
        plt.ylabel("Average runtime [s]")
        plt.semilogx()
        plt.semilogy()
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join("plots", f"{case}.png"))
        plt.close()
