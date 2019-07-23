
import subprocess
import os
import shutil

#requires installing qpdf (http://qpdf.sourceforge.net/) and xpdf tools (https://www.xpdfreader.com/download.html)

#decrypt pdfs with qpdf
for entry in os.scandir('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs/'):
	dec = os.path.splitext(os.path.basename(entry.path))[0]
	dec_path = '/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs/' + dec + '_dec.pdf'
	subprocess.call(['qpdf', '--decrypt', entry.path, dec_path])

#create separate directory for decrypted pdfs
os.makedirs('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs_decrypted/')
for file in os.listdir('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs/'):
	filename = os.path.join('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs/', file)
	if filename.endswith('_dec.pdf'):
		file_dest = '/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs_decrypted/' + os.path.basename(filename)
		shutil.move(filename, file_dest)

#convert decrypted pdfs into txt files with pdftotext
for entry in os.scandir('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs_decrypted/'):
	subprocess.call(['pdftotext', entry.path])

#create separate directory for txt files
os.makedirs('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/txts/')
for file in os.listdir('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs_decrypted/'):
	filename = os.path.join('/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/pdfs_decrypted/', file)
	if filename.endswith('_dec.txt'):
		file_dest = '/home/ayan-yue/Documents/projects/dynamic-word-embeddings/command-papers/txts/'
		shutil.move(filename, file_dest)

