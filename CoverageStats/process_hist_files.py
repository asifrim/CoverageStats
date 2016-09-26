import numpy as np
import pandas as pd
import os
import sys
import pybedtools

def split_hist(hist_path):
	tmp_all_path = "/tmp/"+os.path.basename(hist_path).strip(".gz")+".all.gz"
	tmp_interval_path = "/tmp/"+os.path.basename(hist_path).strip(".gz")+".intervals.gz"
	command_intervals = "zcat "+hist_path+" | awk  '$1 != \"all\"' | sort | uniq | gzip > "+tmp_interval_path
	command_all = "zcat "+hist_path+" | awk  '$1 == \"all\"' | sort | uniq | gzip > "+tmp_all_path	
	os.popen(command_intervals).read()
	os.popen(command_all).read()
	return (tmp_all_path,tmp_interval_path)

def process_intervals(interval_path):
	hist = pd.read_table(interval_path,compression="gzip",header=None,names=("chrom","start","stop","depth","bases_at_depth","length","percentage_at_depth","cumsum"),low_memory=False)
	groups = hist.groupby(["chrom","start","stop"])

	for name,group in groups:
		res = {}
		(res["chrom"],res["start"],res["end"]) =  name
		# res["less_than_5x"] = np.sum(group.ix[group.depth <= 5,"percentage_at_depth"])
		# res["lower_than_20x"] = np.sum(group.ix[group.depth < 20,"percentage_at_depth"])
		group = group.sort("depth")
		group["cumsum"] = np.cumsum(group.ix[:,"percentage_at_depth"])
		res["median"] = group[group["cumsum"] >= 0.5].iloc[0]["depth"]
		
		print "%(chrom)s\t%(start)s\t%(end)s\t%(median)s" % res

def process_all(all_path):
	hist = pd.read_table(interval_path,compression="gzip",header=None,names=("all","depth","bases_at_depth","length","percentage_at_depth","cumsum"),low_memory=False)
	hist = hist.sort("depth")
	hist["cumsum"] = np.cumsum(hist.ix[:,"percentage_at_depth"])
	res["median"] = hist[hist["cumsum"] >= 0.5].iloc[0]["depth"]	
	print "all\t%(median)s" % res

def main():
	(tmp_all_path,tmp_interval_path) = split_hist(sys.argv[1])
	process_intervals(tmp_interval_path)
	os.remove(tmp_all_path)
	os.remove(tmp_interval_path)

if __name__ == "__main__":
	main()
