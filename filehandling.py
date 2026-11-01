from pathlib import Path
def filehandling():
    print("heyy , welcome to the file handling")
    name=input("enter the name of file:")
    path=Path(name)
    try:
        ans=int(input("1:check that is this file existing\n2:go out from handling"))
        if ans == 1:
            if path.exists():
                print("file is existing")
                try:
                    read=int(input("1:want to read file\n2:want to rewrite file\n3:want to add some data in file\n4:want to delete file"))
                    if read == 1:
                        with open(path,"r") as f:
                            print(f.read())
                    elif read == 2:
                        with open(path,"w") as f:
                            data=input("enter the data you want to write in your file:")
                            f.write(data)
                    elif read == 3:
                        with open(path,"a") as f:
                            data=input("enter the data you want to append in your file:")
                            f.append(data)
                    elif read==4:
                        path.unlink()
                        print("your file successfully deleted")
                    else:
                        print("enter the option which is avalible")
                except:
                    print("your ans should be numeric")
            else:
                print("file is not existing")
                try:
                    no=int(input("1:create file\n2:don't wnat to creat file"))
                    if no == 1:
                        with open(path,"w") as f:
                            data=input("enter the data you want to add in file:")
                            f.write(data)
                            print("file create successfully")
                    elif no== 2:
                        pass
                    else:
                        print("entered option is not avalibale")
                except:
                    print("your and must be inntiger")
        elif ans == 2:
            pass
        else:
            print("entered the option is not avalible")
    except:
        print("your ans should be numeric")

filehandling()