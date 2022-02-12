import qrcode


def get_qrcode(url='https://google.com', name="default"):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was generated! Open the {name}.png'


def main():
    print(get_qrcode(url='https://github.com/vvsalwayscodin', name="github"))


if __name__ == '__main__':
    main()
