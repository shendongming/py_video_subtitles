#coding:utf-8
'''
字幕提取测试
'''
import sys
import os.path
import time
import cv
print locals()
fname=  os.path.dirname(__file__)+'/../test_video/1.mp4'
imgpath=os.path.dirname(__file__)+'/../test_img/'
print fname



fp=cv.CreateFileCapture(fname)
#视频测试
#fp=cv.CreateCameraCapture(0)
cv.SetTrackbarPos


img=cv.QueryFrame(fp)

start_height=370;
subtitles_range=(0,start_height,img.width,img.height-start_height)

t1=time.time()
cv.SetCaptureProperty(fp, cv.CV_CAP_PROP_POS_FRAMES,5000);
 
print time.time()-t1	

def diff_img(img1,img2):
	diff=0
	
	t1=t2=0
	for x in range(img1.width):
		for  y in range(img1.height):
			
			
			
			if sum(cv.Get2D(img1,y,x))>0:
				#print cv.Get2D(img1,y,x)
				t1+=1
			 
			if sum(cv.Get2D(img2,y,x))>0:
				#print cv.Get2D(img2,y,x)
				t2+=1

	
	return abs(t1-t2)
last_img=False;
j=0
for i in range(1000):
	img=cv.QueryFrame(fp)
	
			#print p
		#print x,t
	#cv.ShowImage('test',img)
	#CloneImage
	src = cv.GetSubRect(img,subtitles_range )
	y=12
	#print y,src.height
	t=0;
	x=100
	 
	for x in range(src.width):
		p =cv.Get2D(src,y,x)

		t=t+ sum( p)


		if sum(p)>50:

			p1=(x,y+25)
			p2=(x,y+30)
			#print  x,y,t,p,p1,p2
			#cv.Line(src,p1,p2,(0,255,0,0))
			
			break
	#cv.SaveImage('../test_img/test%d.png' % i,img)
	
	if t==0:
		continue

	 
	

	#imgstr= src.tostring()
	if not last_img  :
		print src
		last_img=cv.CloneImage(cv.GetImage(src))
		j=j+1
		print  "write img",j
		cv.SaveImage( (imgpath+'/test%d.png' % (j,)),src)
		continue

	diff=diff_img(last_img,cv.GetImage(src))
	
	if diff >560:
		print 'diff',diff
		print 'change last'
		print src
		last_img=cv.CloneImage(cv.GetImage(src))
		j=j+1
		print  "write img",j
		cv.SaveImage( (imgpath+'/test%d.png' % (j,)),src)

	
	continue
	break
	#value=cv.Get2D(img,y,x)
	
