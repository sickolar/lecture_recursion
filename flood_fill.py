import matplotlib.pyplot as plt

def flood_fill(obraz, x, y):

    if x > len(obraz) - 1:
        return obraz
    elif y > len(obraz[0]) - 1:
        return obraz
    else:
        obraz[x,y] = 2
        obraz = flood_fill(obraz, x + 1, y)
        obraz = flood_fill(obraz, x, y + 1)
        obraz = flood_fill(obraz, x - 1, y)
        obraz = flood_fill(obraz, x, y + 1)
        return obraz
def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)
    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
