import string
def pangrams(s):
    s=s.lower()
    abc=string.ascii_lowercase
    setabc=set()
    for i in abc:
        setabc.add(i)
    test=set()
    for i in s:
        if i==" ":
            continue
        test.add(i)
    if setabc!=test.intersection(setabc):
        return ('not pangram')
    return 'pangram'

x=pangrams('We promptly judged antique ivory buckles for the next prize')
print(x)
Access to fetch at 'https://api.frosty-night.buzz/subdomains.json?infohash=1bc2759167f7a68088cd3c80cb88a9b93ac20c7e&use-bandwidth=false&use-cpu=true&skip-active-job-search=false&pool=seeder&token=%3C!DOCTYPE%20html%3E%0A%3Chtml%20lang%3D%22en-US%22%3E%0A%3Chead%3E%0A%20%20%20%20%3Ctitle%3EJust%20a%20moment...%3C%2Ftitle%3E%0A%20%20%20%20%3Cmeta%20http-equiv%3D%22Content-Type%22%20content%3D%22text%2Fhtml%3B%20charset%3DUTF-8%22%20%2F%3E%0A%20%20%20%20%3Cmeta%20http-equiv%3D%22X-UA-Compatible%22%20content%3D%22IE%3DEdge%22%20%2F%3E%0A%20%20%20%20%3Cmeta%20name%3D%22robots%22%20content%3D%22noindex%2Cnofollow%22%20%2F%3E%0A%20%20%20%20%3Cmeta%20name%3D%22viewport%22%20content%3D%22width%3Ddevice-width%2Cinitial-scale%3D1%22%20%2F%3E%0A%20%20%20%20%3Clink%20href%3D%22%2Fcdn-cgi%2Fstyles%2Fchallenges.css%22%20rel%3D%22stylesheet%22%20%2F%3E%0A%20%20%20%20%0A%0A%3C%2Fhead%3E%0A%3Cbody%20class%3D%22no-js%22%3E%0A%20%20%20%20%3Cdiv%20class%3D%22main-wrapper%22%20role%3D%22main%22%3E%0A%20%20%20%20%3Cdiv%20class%3D%22main-content%22%3E%0A%20%20%20%20%20%20%20%20%3Ch1%20class%3D%22zone-name-title%20h1%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cimg%20class%3D%22heading-favicon%22%20src%3D%22%2Ffavicon.ico%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20onerror%3D%22this.onerror%3Dnull%3Bthis.parentNode.removeChild(this)%22%20%2F%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20webtor.io%0A%20%20%20%20%20%20%20%20%3C%2Fh1%3E%0A%20%20%20%20%20%20%20%20%3Ch2%20class%3D%22h2%22%20id%3D%22challenge-running%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20Checking%20if%20the%20site%20connection%20is%20secure%0A%20%20%20%20%20%20%20%20%3C%2Fh2%3E%0A%20%20%20%20%20%20%20%20%3Cnoscript%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20id%3D%22challenge-error-title%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22h2%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cspan%20class%3D%22icon-wrapper%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22heading-icon%20warning-icon%22%3E%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fspan%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cspan%20id%3D%22challenge-error-text%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Enable%20JavaScript%20and%20cookies%20to%20continue%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fspan%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%3C%2Fnoscript%3E%0A%20%20%20%20%20%20%20%20%3Cdiv%20id%3D%22trk_jschal_js%22%20style%3D%22display%3Anone%3Bbackground-image%3Aurl(%27%2Fcdn-cgi%2Fimages%2Ftrace%2Fmanaged%2Fnojs%2Ftransparent.gif%3Fray%3D7545f7704d2988af%27)%22%3E%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%3Cdiv%20id%3D%22challenge-body-text%22%20class%3D%22core-msg%20spacer%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20webtor.io%20needs%20to%20review%20the%20security%20of%20your%20connection%20before%20proceeding.%0A%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%3Cform%20id%3D%22challenge-form%22%20action%3D%22%2Ftoken%2F%3F__cf_chl_f_tk%3D6SSq6Taj_s_4s2SkwPZZJfXoVzaXdtb3axnd7s6sLKw-1664803136-0-gaNycGzNCn0%22%20method%3D%22POST%22%20enctype%3D%22application%2Fx-www-form-urlencoded%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cinput%20type%3D%22hidden%22%20name%3D%22md%22%20value%3D%22_SSTCOkuS6SPI1JJoFD2qjjAQp_ko8GNEfeRjHy1UKk-1664803136-0-ARWtVqWBQoVCQhJmTYZ2OR3vhJQwh7RDurNVvUFflGlC28GoGXdUZhzQDS2pgIUDCz6yD4af4iIk8X8-_FNJyMGmDY3pP81OkhafUlwXu72fF_OQnPBtGH2ObqopkYeH1_6ItYa55_Sfw0FRZbkrcG42p4WxPwffhz_iNNWeTo_7_ZST5G66qlTjuOLP1nEtNcp9hI7wLcC2xTRI4acwzsNm0D85lGOxuULMlBsoIcNnwae4gF7J97vIocW1XJ-P_DVstaJHqfNrJRW8DEtt7cBZr-VP9BhDVAA9HQvrqhNNuFySLSTKeqKq8zdbdGzrYQHd_8hlETqAJUo2OQydziYuu8GxYjwsQsGvTG1TP2FjuJ0mdC7aRBys_Duv7QPKMVNnnUJcDxdvFNeXVI8nDesYRkyKxGXWjc0z-mwoZ08FFK8VwytDfP_YiXqq_aJL41_E6SNc8MS0m74sD5sOMDKVZSf9npy5_RXhMo28xSF-vWe6FReyGCMCpMtti9AYOUZciGBMDScBFoloelaWm7SnP7lbfFHQG6otXAXssIVjVAJgPYYYLEOLJVmbSKvTLg%22%20%2F%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cinput%20type%3D%22hidden%22%20name%3D%22r%22%20value%3D%22EX1f37eH7u.wjCZRKdAy5MchGm7Kuz9dJJ29iECNVF8-1664803136-0-AflFnvwPJb67z7zho%2BFYW66txXURQjNtWuVQbzVtlH%2Fv21fr9kMkDJRyPbBmF%2BK8xknYx%2FlnDwQXKJ5Al8k5LoKsLoHB2%2FN1Ay8o30%2FQQIimEWQy7%2FQ%2BE7i%2F9ncH90%2Bopp3zrJbZTqbi836vMqU59U%2BcH5rwPaDGzwEojE%2FCxUQHmA6n6d4Fk43umfvvacSAdqOERTTXCwecs9%2BGe5jjnhh1JcXDImkvwqO1Isrp6S26aqA1Bcq0eiZ16CN8IBe89RaMIdBWqR2VRtSYaQQI%2FL%2FPY3h7IKtUjHXfJTJt2LDh%2Bo5cRPQPdgCpLEKMY7dANPdi3qZvNxyUF5CaGsLp%2Fqpnh7olkol84xbji6UAhnWMZucHWKHmoe46uiC0zadSYboWI23Si5i2yslxydATw%2FEp%2BVYRkKW5OOtNvcltTmKL8UiPe7a6mKNi7RPZDTWyg%2FtpRZtkh3dZWfIiEaE%2BtX43W0%2F2ch9SQNIKZkymOGlXyaJtMcvCc7fytjejrzTYbikJMGgRCZ7f0%2Fv3qcDSqoUB%2FOKKfaiTnOFtH6D21TTs2BQnCL0YU2ZZ4by2C%2FAUJMLhlXFdmN82XGulFM4EozqRfHFO3JslXyM1rpTxkuFl6IiswQmWr8v5k95jqXl%2BONzGDXwE6xZHOw6I40cJiIKlmGi0m4Snuw7WMh%2BRVUT1kXaRrjGZdlYjSV1Y0NQOYhMf8cKpueocWzAyAbLbXzhRuXSS4%2Bqiq2d8dH2QEnNCClh51fvKfF%2FtezqMCihyErw4PMWI8IgKtlbGyNZh3DNpfgUgmGtZi0RFy6g%2By6a%2FBqxWLC2V6MXE1lON1bEJTdO8WBucjseoGdu2EdjvDhT8sQkkmkuJTbR0Mi5Db1fWajE69bCmfCbFDVl0zMOFGTlqUnTM191JO9cbPNva2swuLeUIUCinRNwL08%2BSJVqiulCebi5FN6%2Biy%2B0YVrlxFnjk3GoLNTWSDu6a9rW74dfwhJhWzp1lksmVAU2yn%2BTC4NIsPHUDAEejNNWmFFYFJkWj0bq4xn1uXyIRUWcbY%2BWPhz7lZNc%2BNlXaj6J6PeN92pZkQbBmljn5sUBygA4nxNP%2FM2alc1NP8lrLIFhwbBQLa4AMKE0yQ7q%2F1qmGLM4Xmipl3omENBX0kcGRBxOGB4gWJZdPFBatDh5ud68LgnawU1rEUYI%2B01qL1aYz3SyAXTyei%2BBqPKEFywLD6PhNWR%2FOuDqmCfpwIxITeuxxvaqJC5BM9xjMG6enpHGSAut%2B92HUnBCItKSOC5iPLeGQQNmEJvBxXxuy6UubHznKtCGh6dngOba%2BuWqlXzA4W%2BkzUfgRCFbUGEDUhAHm5t0TEB0aOgwjEAPIMj6XXOPR36Ny82HCmg0ogFE09aPzIG1Ognkk49yw4uqkDIg8Gg8cuvlA%2Fgsg6xN%2FX88Z%2BrLUA2M62xprspsLVbeUlY7h%2FNsxrFXGV228QdM13v%2BWNOZ3naXZsbAYIIGZAZO%2FoRq9tBo6nQhCOY2YF3E3MFKFWiRwEgAjdgHZ%2FInk2jp5KmjwTQCTsJY1Kw8%2FKsnkELJJUz650H7iRofY%2BZfErQ0ooskWtCfvYHl3VfneyYuZkLuRYN%2FD3DS9Fj2BYYEIsdxP%2BioGxYyupD%2FurE%2FKwd0GqxnQTm7X5gyZWRRl2UO2WtAABL3kWhJCRAngVhmziqKzjjgNBQo%2FYMJDYJphtz9VJKT7FSTf7gloXb9uVnjXUkhcSjC4JYkIwsjcXkIO0yiABnA%2F31qDxicIrrzoUR4T%2Bj%2BBzfWv4VxyN0hpMPP4M5tuKGJdzMfWtzf0bfk8%2BcQ0oIwYDRIYyjyUUHp6FSeiZfDP2%2F41Dx9f%2BnlygEAwSxtjMqFlaxFD5CA8ZswVJEhuicZlsSzk2kJliqJMgwDqAAYyxPsC4ISpm0wZ6BhuSMtGjsd%2BQLDx9LWccP4jCaxuGN5agFfHEBmtM0XJYU9OcWYH3IY1Gy0Kpn%2Ft%2FfW7wXYUpIIv3uYbUavsJDGAxwh%2F0UngoPFDO74fUCB41VsKGteVaKQQGmh6jigwE9lFIJFTyjtvpIMoYv3UrvvzNDMQgNM3L00W%2FCCY1TRwC%2BoHH4EeCFxoo96snXb7E%2BbovKtPI3Tb2kjhuFpNb4uhOL0S23hfSrzRl%2BBkrkBA59fFTNvflPn26IeS7Vx6TkykZ4OItKMOclCxuiHT%2FI2FTjcbhz0uVf0IfwQRsxGSAYYYPq3poo4tjHiO806t5zNOuym0Ha5x7hcDAZIX5uBQVCA8Pu2jiydXQtdrnDXpyvZjXlcNUxc1%2B0mC91REsElqSaAgPTuOBtdXzK1bsmlf0NDtAHgTVclHfHnBerrNvW%2BDySA51g%2FGYkS%2FHrOt%2BBJGndN4MqMbF4B2yPDrnMtAilIugkxIirdyUu33XVn1ui%2FzvqvrEeViu7eCjk6ujk8jadJDk00mKNEFIwKJByjWHZAx6QgPzuQQnj8lWUIIzzUAikD0ISBNAog0lE9DwJCa%2B2%2FhVqtsSWes0WPfMOsUY5Q%2Fl8acQzuOsPHcjVPOwiVBsy8AaG9yRtODM7OsWkr2W8XY0W8FSYxQ8bWK3Q8OXt8MmL48pAV8vnGCj%2F7ZoQw1dMq5ZGE7eAifs1xAMqqOFu9RXA%3D%3D%22%2F%3E%0A%20%20%20%20%20%20%20%20%3C%2Fform%3E%0A%20%20%20%20%3C%2Fdiv%3E%0A%3C%2Fdiv%3E%0A%3Cscript%3E%0A%20%20%20%20(function()%7B%0A%20%20%20%20%20%20%20%20window._cf_chl_opt%3D%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20cvId%3A%20%272%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cType%3A%20%27managed%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cNounce%3A%20%271474%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cRay%3A%20%277545f7704d2988af%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cHash%3A%20%27f52d76df0d9be44%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cUPMDTk%3A%20%22%5C%2Ftoken%5C%2F%3F__cf_chl_tk%3D6SSq6Taj_s_4s2SkwPZZJfXoVzaXdtb3axnd7s6sLKw-1664803136-0-gaNycGzNCn0%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cFPWv%3A%20%27b%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cTTimeMs%3A%20%271000%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cTplV%3A%204%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cTplB%3A%20%27cf%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20cRq%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ru%3A%20%27aHR0cHM6Ly93ZWJ0b3IuaW8vdG9rZW4v%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ra%3A%20%27TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20rm%3A%20%27R0VU%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20d%3A%20%27uS9fmpxoY739Sqwuc39OtMzQLn9L8EP%2BfP6Ikwd0tsZHAy9ervt1mgAF85Qq5hWXlfadIjwTCxVuItm5MZBY3eqGkNKvHAgUhYO05nAsEJE9qfTkMXPBFEuOE1NXUMIJfF0ovinOFI20d2CAbvCrRz8nWv0lPt4V7Ql7Ntq%2F4a%2FIL89Dc3CnYzpJoSaCyYUTaEbonGkiY57ukUVZSGJiPugbvBD0%2FG80zy5Y3sh2vRwivPmYFi7pZgDrPHEQvyV91y460l1F5vwSnMy9uUjy6BD4WKaRAL1BGI8ARWwXUv5orog64YBnlzFLYZO8wEKKMp%2BVw2xTVNtXmeV691MFfYAitDO20jQg%2FjiiiJFb4r5QWsta2unjH5IUy7q9NtptL2lTWEbwgUz%2F8%2Fx8vYszPhz%2FdsxJPjvhyau7Gs591z7X9U6P8NiK20OwmvUzih5Qff5JgVGfTK0axKn%2Fh4ZyBWxOTTpFrOjpw2XFYZXynIX4hu8vIqgun4z0EAI5VX0PQnxl70gAlPeuDEiD7aFAYOIh88dIh8zOtKQxsNPwKdUi0VDwUCW%2Bi88PzuCoIIXgPAwqT0%2FdMvnIG1MbjcRhzw4vU1n8QaW7O%2F9aP9sbraE%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20t%3A%20%27MTY2NDgwMzEzNi4wNjgwMDA%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20m%3A%20%27t%2BIhGJbBkLHckjGJBR1pUxa3jj2LVxfqN11FEHaUuWE%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i1%3A%20%27rhhGfjvVMl%2B2EdnXcv%2BIHQ%3D%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i2%3A%20%27FCmdS0C5hztKSYItyCHnKg%3D%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20zh%3A%20%27POkls74yjAWPS8RRCBnnc93dJ7PwF6nGy0k7%2FvqJ9sE%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20uh%3A%20%27HZL1KRhXOQOkEniYBm1JExUUTMI8JHb4%2BDBxUC9Snyk%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20hh%3A%20%274CeM8HtIR%2BHduGLfGnsnun%2BxzGY%2B%2BAhcockKw1rrtcc%3D%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%3B%0A%20%20%20%20%20%20%20%20var%20trkjs%20%3D%20document.createElement(%27img%27)%3B%0A%20%20%20%20%20%20%20%20trkjs.setAttribute(%27src%27%2C%20%27%2Fcdn-cgi%2Fimages%2Ftrace%2Fmanaged%2Fjs%2Ftransparent.gif%3Fray%3D7545f7704d2988af%27)%3B%0A%20%20%20%20%20%20%20%20trkjs.setAttribute(%27style%27%2C%20%27display%3A%20none%27)%3B%0A%20%20%20%20%20%20%20%20document.body.appendChild(trkjs)%3B%0A%20%20%20%20%20%20%20%20var%20cpo%20%3D%20document.createElement(%27script%27)%3B%0A%20%20%20%20%20%20%20%20cpo.src%20%3D%20%27%2Fcdn-cgi%2Fchallenge-platform%2Fh%2Fb%2Forchestrate%2Fmanaged%2Fv1%3Fray%3D7545f7704d2988af%27%3B%0A%20%20%20%20%20%20%20%20window._cf_chl_opt.cOgUHash%20%3D%20location.hash%20%3D%3D%3D%20%27%27%20%26%26%20location.href.indexOf(%27%23%27)%20!%3D%3D%20-1%20%3F%20%27%23%27%20%3A%20location.hash%3B%0A%20%20%20%20%20%20%20%20window._cf_chl_opt.cOgUQuery%20%3D%20location.search%20%3D%3D%3D%20%27%27%20%26%26%20location.href.slice(0%2C%20-window._cf_chl_opt.cOgUHash.length).indexOf(%27%3F%27)%20!%3D%3D%20-1%20%3F%20%27%3F%27%20%3A%20location.search%3B%0A%20%20%20%20%20%20%20%20if%20(window.history%20%26%26%20window.history.replaceState)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20ogU%20%3D%20location.pathname%20%2B%20window._cf_chl_opt.cOgUQuery%20%2B%20window._cf_chl_opt.cOgUHash%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20history.replaceState(null%2C%20null%2C%20%22%5C%2Ftoken%5C%2F%3F__cf_chl_rt_tk%3D6SSq6Taj_s_4s2SkwPZZJfXoVzaXdtb3axnd7s6sLKw-1664803136-0-gaNycGzNCn0%22%20%2B%20window._cf_chl_opt.cOgUHash)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20cpo.onload%20%3D%20function()%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20history.replaceState(null%2C%20null%2C%20ogU)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20document.getElementsByTagName(%27head%27)%5B0%5D.appendChild(cpo)%3B%0A%20%20%20%20%7D())%3B%0A%3C%2Fscript%3E%0A%0A%20%20%20%20%3Cdiv%20class%3D%22footer%22%20role%3D%22contentinfo%22%3E%0A%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-inner%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22clearfix%20diagnostic-wrapper%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22ray-id%22%3ERay%20ID%3A%20%3Ccode%3E7545f7704d2988af%3C%2Fcode%3E%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22text-center%22%3EPerformance%20%26amp%3B%20security%20by%20%3Ca%20rel%3D%22noopener%20noreferrer%22%20href%3D%22https%3A%2F%2Fwww.cloudflare.com%3Futm_source%3Dchallenge%26utm_campaign%3Dm%22%20target%3D%22_blank%22%3ECloudflare%3C%2Fa%3E%3C%2Fdiv%3E%0A%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%0A%20%20%20%20%3C%2Fdiv%3E%0A%3C%2Fbody%3E%0A%3C%2Fhtml%3E%0A&api-key=8acbcf1e-732c-4574-a3bf-27e6a85b86f1' from origin 'https://webtor.io' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.