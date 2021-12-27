# Modules
import os
import configparser

#Variables
USERPROFILE=os.environ['USERPROFILE']
APPDATA=os.environ['APPDATA']

# Check if "Options.ini" exists or not.
def ConfigExist():
    if os.path.isfile("Options.ini") is False:
        ConfigCreate()
        
# Create a "Options.ini" file.    
def ConfigCreate():
    config = configparser.ConfigParser()
    config['Minecraft'] = {'1.7 Directory': APPDATA+"\\.minecraft",
                           '1.8 Directory': APPDATA+"\\.minecraft",
                           '1.12 Directory': APPDATA+"\\.minecraft",
                           '1.16 Directory': APPDATA+"\\.minecraft",
                           '1.17 Directory': APPDATA+"\\.minecraft",
                           '1.18 Directory': APPDATA+"\\.minecraft"
                           }
    config['Java'] = {'Arguments': "-Xms3G -Xmx3G -Xmn1G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M",
                      '1.7 Java': USERPROFILE+"\\.lunarclient\\jre\\1.7\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.8 Java': USERPROFILE+"\\.lunarclient\\jre\\1.8\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.12 Java': USERPROFILE+"\\.lunarclient\\jre\\1.12\\zulu16.30.15-ca-fx-jre16.0.1-win_x64\\bin\\javaw.exe",
                      '1.16 Java': USERPROFILE+"\\.lunarclient\\jre\\1.16\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.17 Java': USERPROFILE+"\\.lunarclient\\jre\\1.17\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.18 Java': USERPROFILE+"\\.lunarclient\\jre\\1.18\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      }
    config['Optimizations'] = {'LC Cosmetics' : "On"}
    with open('Options.ini', 'w') as configfile:
        config.write(configfile)
        
# Read Values from "Options.ini".       
def ConfigRead(Version):
    
    ConfigExist()
    config = configparser.ConfigParser()
    config.read('Options.ini')
    Arguments_String=config['Java']["Arguments"]
    Arguments_List=Arguments_String.split()
    
    # 1.7
    if Version=="1.7":
        Java_Path=config['Java']["1.7 Java"]
        Directory=config['Minecraft']["1.7 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
        
    # 1.8    
    elif Version=="1.8":
        Java_Path=config['Java']["1.8 Java"]
        Directory=config['Minecraft']["1.8 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
        
    # 1.12    
    elif Version=="1.12":
        Java_Path=config['Java']["1.12 Java"]
        Directory=config['Minecraft']["1.12 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
        
    # 1.16    
    elif Version=="1.16":
        Java_Path=config['Java']["1.16 Java"]
        Directory=config['Minecraft']["1.16 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
        
    # 1.17    
    elif Version=="1.17":
        Java_Path=config['Java']["1.17 Java"]
        Directory=config['Minecraft']["1.17 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']
        
    # 1.18    
    elif Version=="1.18":
        Java_Path=config['Java']["1.18 Java"]
        Directory=config['Minecraft']["1.18 Directory"]
        Cosmetics=config['Optimizations']['LC Cosmetics']

    # Return Values
    return [Cosmetics, Java_Path, Directory, Arguments_List]
