 # https://doi.org/10.1016/j.neucom.2012.02.053
 # [0.0625, 0.0625, 0.125, 0.25, 0.5] for 5 fold

 def weighted_average(k):
  # k : fold 數
 	w = []
 	n = len(k)
 	for j in range(1, n + 1):
 		j = 2 if j == 1 else j
 		w.append(1 / (2**(n + 1 - j)))
 	return np.average(k, weights = w)
