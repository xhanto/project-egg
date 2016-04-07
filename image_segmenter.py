import cv2
filep = raw_input("Enter file path + name (no ext): ")
res = "segmentataion"
img = cv2.imread(filep+".png")
rows,cols,channels = img.shape
for k in range(rows/16):
    for l in range(cols/16):
        square = img[16*k:16*(k+1),16*l:16*(l+1)]
        title = "segmentation\seg_%s_%s.png" % (k+1,l+1)
        cv2.imwrite(title,square)
