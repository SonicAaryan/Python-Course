def main():
    try:
        a = int(input("Hey Enter a number :"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("Hey I'll run even if u return me!! that's my purpose")

main()
        