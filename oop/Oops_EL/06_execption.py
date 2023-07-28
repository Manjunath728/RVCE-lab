while True:
    ch=int(input("\n1.ZeroDivisionError\n2.ImportError\n3.AttributeError\n4.IndexError\n5.KeyError\nEnter choice:"))
    try:
        if ch==1:
            result = 1 / 0
        if ch==2:
            import nonexistent_module
        if ch==3:
            obj = "hello"
            obj.foo()
        if ch==4:
            lst = [1, 2, 3]
            value = lst[4]
        if ch==5:
            dct = {"name": "John", "age": 25}
            value = dct["city"]
    except ZeroDivisionError:
        print("ZeroDivisionError occurred")
    except ImportError:
        print("ImportError occurred")
    except AttributeError:
        print("AttributeError occurred")
    except IndexError:
        print("IndexError occurred")
    except KeyError:
        print("KeyError occurred")