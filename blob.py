import requests
import os
import jsbeautifier
from javascript import require

class Blob:
    def __init__(self, version):
        self.version = version
        
    def fetcher(self):
        hsw = requests.get(f"https://newassets.hcaptcha.com/c/{self.version}/hsw.js").text.strip()    
        protection = False
        if ");try{crypto[" in hsw:
            protection = True
            
        return hsw, protection
    
    def modify(self):
        self.hsw, protection = self.fetcher()
        if protection:
            p1 = self.hsw.split(");try{crypto[")[0]
            p2 = self.hsw.split(");try{crypto[")[1].split("}catch(A){}")[1]
            self.hsw = f"{p1});{p2}"
        func = self.hsw.split('"2870177450012600261");function ')[1].split("(")[0].strip()
        self.hsw = self.hsw.replace("if(0===A)", f"if(2===A)return {func}(new TextEncoder().encode(Q));if(0===A)")
        with open(f"./archive/{self.version}.js", 'w') as f:
            f.write(jsbeautifier.beautify(self.hsw))
        return self.hsw
    
    def encrypt(self, data):
        self.jsdom = require('jsdom')
        self.evaluate = require("vm").Script
        self.vm = self.jsdom.JSDOM("<title></title>", {"runScripts": "dangerously"}).getInternalVMContext()
        if os.path.exists(f"./archive/{self.version}.js"):
            hsw = open(f"./archive/{self.version}.js", 'r').read()
        else:
            hsw = self.modify()
        self.evaluate(hsw).runInContext(self.vm)
        result = self.evaluate(f"hsw(2, '{data}')").runInContext(self.vm)
        print(f"Blob -> {result}")
        return result
    
v = 'b6c577e821782d165391120f81927bb93c6711d2891662a8345de7f9eb701145'
    
Blob(v).encrypt("")
