import argparse
import colorama 
import googlesearch
import os ; import time
from colorama import Fore , Back
from datetime import datetime
colorama.init(autoreset=True)

fg_colors = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'blue' : Fore.CYAN,
    'yellow': Fore.YELLOW
}

parser = argparse.ArgumentParser(description='A tool that searches URLs with dork is typically used for reconnaissance or information gathering purposes. The tool allows users to search for specific web pages or files on a website using a dork, which is a specific search query that can be used to find information that is not easily found through normal search engine queries.')
parser.add_argument('-d' , '--dork' , help='return target dork to you want ' , type=str)
parser.add_argument('-n' , '--num' , help='return number result to you want ' , type=int)
parser.add_argument('-l' , '--lang' , help='return language urls to you want ' , default='en' , type=str)
parser.add_argument('--save' , action='store_true' , help='save all result in file text')
args = parser.parse_args()

dork_user = args.dork
num_user = args.num
lang_user = args.lang
save_user = args.save

proxie = {
    'http': 'http://163.44.253.160:80',
    'https': 'https://163.44.253.160:80',
}
def AliMabrouk():
    urls = list()
    try :
        if dork_user and num_user : 
            for i in googlesearch.search(dork_user , num_results=num_user , lang=lang_user):
                print(f'{fg_colors["green"]}[+] [>] {i}')
                time.sleep(1)
                urls.append(f'{i}\n')
        if save_user :
            if not os.path.exists('results'):os.mkdir('results')
            date_now = datetime.now()
            strftime = date_now.strftime('%d/%m/%Y %H:%M:%S')
            with open('results/index.txt' , 'a') as my_file : 
                my_file.write(f'{strftime} \n')
                my_file.write(''.join(urls))
                my_path = os.getcwd() +r"\results\index.txt"      
                print(f'Results saved successfully in path {fg_colors["blue"]+ my_path} ')
    except Exception as main_erro :
        print(f'{fg_colors["red"]}[!] Too Many Requests for url Please Try Again')

AliMabrouk()
input('Press Enter To Exit ....')

