#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import argparse
import sys
from collections import namedtuple

sl_list_descr = {"1"  : "BHO, Toolbars, URLSearchHooks, Explorer Bars",
             "2"  : "Startup / Autorun Entries",
             "3"  : "Internet Explorer Buttons",
             "9"  : "LSPs",
             "10" : "DPF ActiveX Installs",
             "4"  : "Extra Protocols",
             "5"  : "AppInit_DLLs & Winlogon Notify",
             "6"  : "ShellServiceObjectDelayLoad",
             "7"  : "Shared Task Scheduler",
             "8"  : "Services",
             "11" : "ShellExecuteHooks",
             "12" : "Drivers",
             "13" : "Firefox Extensions",
             "14" : "Active Setup"}

sl_list2param = {"CLSID"   :  "1", "O2" : "1", "O3" : "1", "R3" : "1",
            "STARTUP" :  "2", "O4" : "2",
            "O9"      :  "3",
            "O10"     :  "9", "LSP" : "9",
            "O16"     : "10",
            "O18"     :  "4",
            "O20"     :  "5",
            "O21"     :  "6",
            "O22"     :  "7",
            "O23"     :  "8", "SERVICES" : "8",
            "SEH"     : "11",
            "DRIVERS" : "12",
            "FF"      : "13", "FIREFOX" : "13",
            "ACTIVE"  : "14"
            }

type_list = {"filename", "clsid", "name"}

# Create Type for search results
SearchResult = namedtuple("SearchResult", "clsid name filename description status")

def extract_results(soup):
    data = []
    table = soup.find('table', attrs={'class':'resultsTables'})

    if table:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [elem.text.strip() for elem in cols]
            data.append(cols)
        del data[0] # remove table title
        data = map(row2result, data) # convert rows to search result objects
    return data

def row2result(row):
    if len(row) == 5:
        return SearchResult(row[0], row[1], row[2], row[3], row[4])
    else:
        return SearchResult(None    , row[0], row[1], row[2], row[3])

def print_results(results):
    for res in results:
        print_title(res.name + ", " + res.status)
        if res.clsid:
            print "CLSID:", res.clsid
        print "Filename:", res.filename
        print "Description:", res.description
        print
    if not results:
        print "no results"
        print

def parse_arguments():
    parser = argparse.ArgumentParser(description="SystemLookup.com Command Line Tool", prog="systemlookup.py")
    parser.add_argument("-l", "--list", help="The list that is used to lookup the entry. Possible values: " + ", ".join(sl_list2param.keys()), dest="sl_list")
    parser.add_argument("-t", "--type", help="The type of the search item. Possible values: " + ", ".join(type_list), dest="searchtype", required=True)
    parser.add_argument("searchitem")
    args = parser.parse_args()
    if args.sl_list and not args.sl_list.upper() in sl_list2param:
        parser.print_usage()
        raise ValueError("error: invalid list, possible values: " + ", ".join(sl_list2param.keys()))
    if not args.searchtype in type_list:
        parser.print_usage()
        raise ValueError("error: invalid search type, possible values: " + ", ".join(type_list))
    return args

def syslookup(listnr, chosentype, search_term):
    base_url = "http://www.systemlookup.com/"
    sl_list = "lists.php?list=" + listnr
    sl_type = "type=" + chosentype
    sl_search= "search=" + search_term
    return requests.get(base_url + sl_list + "&" + sl_type + "&" + sl_search + "&s=").text

def print_title(title, big=False):
    if big:
        title = "|| " + title + " ||"
        print "-" * len(title)
    print title
    print "-" * len(title)
    print

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        args = parse_arguments()
        lists = []
        # list specific search
        if args.sl_list:
            lists.append(sl_list2param[args.sl_list.upper()])
        # global search, add all lists
        else:
            for listnr in sl_list_descr.keys():
                lists.append(listnr)

        # get and print results for each list
        for listnr in lists:
            # request data from systemlookup.com
            data = syslookup(listnr, args.searchtype, args.searchitem)
            soup = BeautifulSoup(data)
            listname = sl_list_descr[listnr]
            results = extract_results(soup)
            if results:
                print_title("List: " + listname, big=True)
                print_results(results)
            else:
                print listname + ":", "no results"
                print
    except ValueError as e:
        print >> sys.stderr, e
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())

