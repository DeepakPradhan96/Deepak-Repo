from configparser import ConfigParser
#object
config=ConfigParser()

#to read Data From Config File
#config.read('C:/Users/deepaak/PycharmProjects/TestAutomation Tw/Config.cfg')
config.read('./InputFiles/config.cfg') #./ represnt current path

print(config.get('section1','username'))

print(config.get("Hellow",'password'))
print(config.get('Hellow','dsr'))