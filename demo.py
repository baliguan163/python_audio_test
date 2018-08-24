# -*- coding: UTF-8 -*-
import pylab
pylab.subplot(1, 3, 1);
pylab.axis('off');
pylab.imshow(img)
pylab.gray()
pylab.subplot(1, 3, 2);
pylab.axis('off');
pylab.imshow(filtered_img[0, 0, :, :])
pylab.subplot(1, 3, 3);
pylab.axis('off');
pylab.imshow(filtered_img[0, 1, :, :])
pylab.show()
