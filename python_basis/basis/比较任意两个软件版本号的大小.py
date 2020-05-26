print("请输入version1>>>")
version1 = input()
version1Str = ''.join(version1.split('.'))
print("请输入version2>>>")
version1StrLength = len(version1Str)
version2 = input()
version2Str = ''.join(version2.split('.'))
version2StrLength = len(version2Str)
maxVersion = 0
if version1StrLength == version2StrLength:
    maxVersion = max([eval(version1Str), eval(version2Str)])
elif version1StrLength > version2StrLength:
    num = version1StrLength - version2StrLength
    version2StrNew = version2Str + num * '0'
    maxVersion = max([eval(version1Str), eval(version2StrNew)])
else:
    num = version2StrLength - version1StrLength
    version1StrNew = version1Str + num * '0'
    maxVersion = max([eval(version1StrNew), eval(version2Str)])
if maxVersion == version1Str:
    print("maxVersion:", version1)
elif maxVersion == version2Str:
    print("maxVersion:", version2)
elif str(maxVersion).strip('0') == version1Str:
    print("maxVersion:", version1)
elif str(maxVersion).strip('0') == version2Str:
    print("maxVersion:", version2)