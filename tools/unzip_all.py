import sys
import os
from pathlib import Path

def unzip(dst, src):
	try:
		src_path_full = os.path.abspath(src)
		sources = os.listdir(src_path_full)
		sources = [(src_path_full + '/' + i) for i in sources ]
	except:
		raise Exception("incorrect source dir", src_path_full)
	
	try:
		dst_path_full = os.path.abspath(dst)
	except:
		raise Exception("incorrect dst dir", dst_path_full)

	test_file_create = str("touch " + dst_path_full + '/tester_file')
	test_file_delete = str("rm " + dst_path_full + '/tester_file')
	try:
		os.system(str(test_file_create))
		os.system(str(test_file_delete))
	except:
		raise Exception("source dir not accessible",  dst_path_full)

	zip_files = []
	for i in sources:
		try:
			ext = os.path.splitext(i)[1]
			if ext == '.zip':
				zip_files += [i]
		except:
			raise Exception("unexpected error")

	for zip_file in zip_files:
		try:
			os.system(str('unzip {} -d {}'.\
						format(zip_file, dst_path_full + '/' + Path(zip_file).stem)))
		except:
			raise Exception("unzip error")
	print('Done!')

def main(args):
	if len(args) != 3:
		raise Exception("not enough args")
	unzip(args[2], args[1])

if __name__ == "__main__":
	main(sys.argv)
