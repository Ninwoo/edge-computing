def make(name,text):
        try:
                f=open(name,'a')
                f.write(text)
                f.close()
        except IOError:
                pass

