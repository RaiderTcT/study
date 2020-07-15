from PIL import Image

im_1 = Image.open('thumbnail.jpg')
print('im_1 mode:', im_1.mode)
im_2 = Image.open('hong.jpeg')
print('im_2 mode:', im_2.mode)
w, h = im_1.size
print('image size 1:%s, %s' % (w, h))
w, h = im_2.size
print('image size 2:%s, %s' % (w, h))
# 缩放
# im.thumbnail((700, 452))
#
# 旋转逆时针
# im_1.rotate(180).show()
#
# Alpha composite im2 over im1.
# Image.alpha_conposite(im_1, im_2)
#
#
# 合成，alpha：透明度 out = image1 * (1.0 - alpha) + image2 * alpha
im = Image.blend(im_1, im_2, 0.5)

im = Image.composite(im_1, im_2)

# 保存
im.save('hecheng.jpeg', 'jpeg')
