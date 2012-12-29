#coding:utf-8
'''
字幕提取测试
'''
import sys
import os.path
import time
import cv

fname=  os.path.dirname(__file__)+'/../test_video/1.mp4'
imgpath=os.path.dirname(__file__)+'/../test_img/'
#print fname

fp=cv.CreateFileCapture(fname)
#视频测试
#fp=cv.CreateCameraCapture(0)
#cv.SetTrackbarPos

img=cv.QueryFrame(fp)

start_height=210;
start_left=200;
subtitles_range=(start_left,start_height,img.width-start_left,img.height-start_height)

t1=time.time()
cv.SetCaptureProperty(fp, cv.CV_CAP_PROP_POS_FRAMES,500);
 
print time.time()-t1	

def diff_img(img1,img2):
	'比较2个图片'
	diff=0
	if abs(img1.width-img2.width) * abs(img1.height-img2.height) >10:
		return 99999
	t1=t2=0
	
	for x in range(min(img2.width,img1.width)):
		for  y in range(min(img2.height,img1.height)):
			t1=t2=0
			if sum(cv.Get2D(img1,y,x))>100 :
				t1=1
			if sum(cv.Get2D(img2,y,x))>100:
				t2=1
				#cv.Set2D(img2,y,x,(255,255,255,0))
			if t1!=t2:
				diff +=1 
	
	return diff

last_img=False;
j=0
max_diff=0

while 1:
	img=cv.QueryFrame(fp)
	if not img:
		print 'done'
		break

	start_x=end_x=0
	for x in range(img.width):
		t=0
		for y in range(370,402):
			p =cv.Get2D(img,y,x)
			t=t+ sum( p)

		if t>1000  :
			if(start_x==0):
				start_x=x
			end_x=x+1	
			
	if start_x==0:
		continue

	#根据扫描结果获取字幕区域
	src=cv.GetSubRect(img,(start_x,370,end_x-start_x,402-370));

	#cv.ShowImage('sub',src)
	#cv.ShowImage('img',img)
	
	#cv.WaitKey(1) 

	if not last_img  :
		last_img=src
		j=j+1
		img_name=imgpath+'/test%04d.png' % (j,)
		print 'save img :',img_name
		cv.SaveImage( img_name,src)
		continue

	#和上一次的比较,是否相同 (近似),生成目标图片
	diff=diff_img(last_img,src)
	max_diff=max(max_diff,diff)
	#比较最近2个图片的差异
	if diff >0:
		print 'diff',diff
	if diff >800:
		last_img=src
		j=j+1
		img_name=imgpath+'/test%04d.png' % (j,)
		print 'save img :',img_name
		print cv.GetCaptureProperty(fp, cv.CV_CAP_PROP_POS_FRAMES);
		cv.SaveImage( img_name,src)
	
