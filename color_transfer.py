import numpy as np
import cv2
#import os

def read_file(sn,tn):
	#s = cv2.imread('source/'+sn+'.bmp')
	s = cv2.imread(sn)
	s = cv2.cvtColor(s,cv2.COLOR_BGR2LAB)
	#t = cv2.imread('target/'+tn+'.bmp')
	t = cv2.imread(tn)
	t = cv2.cvtColor(t,cv2.COLOR_BGR2LAB)
	return s, t

def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2))
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

def color_transfer(sources,targets):
	# sources = ['s1']
	# targets = ['t1']

	for n in range(len(sources)):
		#print("Converting picture"+str(n+1)+"...")
		s, t = read_file(sources[n],targets[n])
		s_mean, s_std = get_mean_and_std(s)
		t_mean, t_std = get_mean_and_std(t)
		# s_mean, s_std = [158.48,126.02,126.33],[14.9,0.64,0.73]
		# t_mean, t_std = [154.35,128.78,123.29],[38.5,0.78,2.99]
		# print(s_mean[0],t_std[0],s_std[0],t_mean[0])
		#print(s_mean,t_std,s_std,t_mean)
		height, width, channel = s.shape
		for i in range(0,height):
			for j in range(0,width):
				for k in range(0,channel):
					x = s[i,j,k]
					#print(x)
					x = ((x-s_mean[k])*(t_std[k]/s_std[k]))+t_mean[k]
					# if i == 0 and j == 0:
					# 	print(s_mean[k],t_std[k],s_std[k],t_mean[k])
					# round or +0.5
					#print(x)
					x = round(x)
					# boundary check
					x = 0 if x<0 else x
					x = 255 if x>255 else x
					s[i,j,k] = x

		s = cv2.cvtColor(s,cv2.COLOR_LAB2BGR)
		#cv2.imwrite('result/r'+str(n+1)+'.bmp',s)
		#cv2.imwrite(f'Image_color_corrected.png',s)
		return s

# color_transfer()
# os.system("pause")