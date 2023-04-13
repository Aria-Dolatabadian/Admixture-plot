import matplotlib.pyplot as plt
import geneview as gv

# load the datasets
with open("admixture_output.Q", "r") as f1, open("admixture_population.info", "r") as f2:
    admixture_output_fn = f1.read()
    population_group_fn = f2.read()

# define the order for population to plot
pop_group_1kg = ["KHV", "CDX", "CHS", "CHB", "JPT", "BEB", "STU", "ITU", "GIH", "PJL", "FIN",
                 "CEU", "GBR", "IBS", "TSI", "PEL", "PUR", "MXL", "CLM", "ASW", "ACB", "GWD",
                 "MSL", "YRI", "ESN", "LWK"]

# plot the admixtureplot using geneview and matplotlib
f, ax = plt.subplots(1, 1, figsize=(14, 2), facecolor="w", constrained_layout=True, dpi=300)
gv.popgene.admixtureplot(data=admixture_output_fn,
                        population_info=population_group_fn,
                        group_order=pop_group_1kg,
                        shuffle_popsample_kws={"frac": 0.5},
                        ylabel_kws={"rotation": 45, "ha": "right"},
                        ax=ax)

plt.show()
