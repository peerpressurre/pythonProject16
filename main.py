try:
    text = input("---")
    somefile = open("hello.txt","w")
    try:
        somefile.write(text)
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)