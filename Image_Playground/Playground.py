from PIL import Image, ImageFilter

def opener():
    inp = input("Enter the image name (Sample images available are: Image1, Image2 & Image3) : ")
    path = fr"C:\Users\HP\Desktop\Placement Projects\Python\Image_Playground\Sample Files\{inp}.jpg"
    img = Image.open(path)
    return img

def gray_scale(img):
    # Convert the image to grayscale
    img_gray = img.convert("L")
    img_gray.save('gray_image.jpg')
    return img_gray

def bilevel(img):
    # Convert the image to bilevel
    bw_gray = img.convert("1")
    bw_gray.save('bilevel_image.jpg')
    return bw_gray

def blur(img):
    # Apply a blur filter to the image
    img_blur = img.filter(ImageFilter.GaussianBlur)
    img_blur.save('blurred_image.jpg')
    return img_blur

def emboss(img):
    # Apply a emboss filter to the image
    img_em = img.filter(ImageFilter.EMBOSS)
    img_em.save('em_image.jpg')
    return img_em

def bg(img):
    # Convert an image into a gradient blend background
    img_bg = img.filter(ImageFilter.BoxBlur(450))
    img_bg.save('em_image.jpg')
    return img_bg

def outline(img):
    # Apply outlines with dark background to the image
    img_ot = img.filter(ImageFilter.FIND_EDGES)
    img_ot.save('ot_image.jpg')
    return img_ot

def main(img):
    
    print("\n The available features are: \n1) Grayscale \n2) Bilevel \n3) Blur \n4) Emboss \n5) Background \n6) Thin Edging \n0) For Previewing original image \n")

    print("Please enter only numeric value to avoid any issues:)")

    value = int(input("Enter the effect you want to try in numeric: "))
    
    if value == 0:
        final = img
    elif value == 1:
        final = gray_scale(img)
    elif value == 2:
        final = bilevel(img)
    elif value == 3:
        final = blur(img)
    elif value == 4:
        final = emboss(img)
    elif value == 5:
        final = bg(img)
    elif value == 6:
        final = outline(img)
    else:
        print("Enter between 1 - 5 only! \n")
        main(img)

    final.show()
    again = input("\nDo you want to continue? \n (y/n): ")
    if again == 'y':
        main(img)
    else:
        exit()


if __name__ == "__main__":
    main(opener())
    