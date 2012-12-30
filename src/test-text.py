#coding:utf-8
'''
图片 转换为文字的测试脚本
'''

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
from os.path import dirname

base_dir=dirname(os.path.realpath(__file__))

import os.path

def write_text():

 
 	p=os.listdir(base_dir+'/../fonts/')
 	print p

 	im=Image.new('RGB', (600,40*len(p)))
 	draw = ImageDraw.Draw(im)
 	font2 = ImageFont.truetype(base_dir+'/../fonts/宋体.ttc',24)
 	print base_dir
 	j=0
 	for f2 in p:
 		
	 	f=base_dir+'/../fonts/'+f2
	 	print f
	 	try:
		 	font = ImageFont.truetype(f,32)
		 	print font
		 	draw.text((10,10+j*40),unicode("这么震憾的场面:"+f2,'utf-8'),font=font)
		 	#draw.text((210,10+j*32),unicode(f2,'utf-8'),font=font2)
		 	j=j+1
		except:
			print 'err',f
			continue
	 	
 	#draw.text((10,40),u"你好中华崛起 hello",font=font)
 	im.show()




def write_font_index():
	'''
	\u4E00-\u9FA5 \uF900-\uFA2D
	'''
	
	def write_font_map(font_size):
		cols_count=64
		font = ImageFont.truetype(base_dir+'/../fonts/华文黑体.ttf',font_size)
		j=0
		chars=range(0x4E00,0x9FA5+1)+range(0xF900,0xFA2D+1)
		im=Image.new('RGB', ((font_size+8)*cols_count+20,(font_size+8)*len(chars)/cols_count))
		#im=Image.new('RGB', (600,100))
	 	draw = ImageDraw.Draw(im)
	 	rows=0
	 	cols=0
		for i in chars:
			cols=j % cols_count
			rows= (j - cols) /cols_count
			j+=1
			draw.text((10+cols*(font_size+8),10+rows*(font_size+8)),unichr(i),font=font)

		im.save(base_dir+'/../fonts/华文黑体.ttf.map.'+str(font_size)+'.png')

	write_font_map(64)
	write_font_map(32)

write_font_index()



#write_text()	


