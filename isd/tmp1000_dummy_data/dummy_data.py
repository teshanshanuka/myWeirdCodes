import numpy as np

drawplots = False
# no_of_datapoints = 2000
#
# ref = np.linspace(25,50, no_of_datapoints)
# ref_noise = np.random.normal(0,0.1, no_of_datapoints)
# ref_orig = ref + ref_noise
#
# print("\nReference noise\n \
#         mean: %.4f\n \
#         stdev: %.3f\n \
#         within expanded uncertainity: %.2f%%\n" % (np.mean(ref_noise), np.std(ref_noise), 100*sum(abs(ref_noise)<0.2)/no_of_datapoints))

ref_reading = np.arange(25,50,0.5)
no_datapoints = ref_reading.shape[0]
ref_orig = np.tile(ref_reading, (100, 1)) + np.random.normal(0, 0.1, (100, no_datapoints))

tmp_err_stdev = 0.05
tmp_reading = ref_orig + np.random.normal(0, tmp_err_stdev, (100, no_datapoints))

print("\nNoise compared to reference thermometer reading\n \
        mean: %.4f\n \
        stdev: %.3f\n " % (np.mean(tmp_reading - ref_reading), np.std(tmp_reading - ref_reading)))

if drawplots:
    # import matplotlib.pyplot as plt
    #
    # plt.hist(ref_noise, bins=50)
    # plt.title("Reference thermometer error distribution")
    # plt.show()
    pass
