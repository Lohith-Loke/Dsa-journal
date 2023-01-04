# KMP
A algo for pattren matching with time complexcity of o(n+m) [n-string , m-pattren]
there is a neassory pre processing steps that needs to be completed before using Algo. 

The pre processing step is called <strong> LSP </strong>

## LSP (Longest Sufix prefix)  
or LPS (Longest prefix suffix ) 
Terminogies
<br>proper prefix <br>
for a string "Hello" 
> prefix - "Hello","Hell","Hel","He","H","" [notice both "",and hello are prefix ]
<br>
proper prefix -"Hell","Hel","He","H","", [notice : Hello is missing]

The length of the longest proper prefix in the (sub)pattern that matches a proper suffix in the same (sub)pattern.

<details>
	<summary>
	LPS of string 'aba'
	</summary>
	consider "aba" <br>
	prefix => a, ab <br>
	sufix => ba, a <br>
	prefix that maches sufix ['a'] 
	longest among them is ('a') with  len = 1
	'' Longest proper prefix that matches a proper suffix for aba is 1 ''
</details>



<details>
	<summary>
	LPS of string "abab"
	</summary>
	LPS of string "abab"
	<summary>
	string - "abab" <br>
	prefix - a, ab,aba <br>
	sufix  - bab,ab,b <br>
	prefix which is also suffix - ['ab'] <br>
	longest among them is ['ab'] with <ins> len -2 </ins>
</details>

<!-- [python] -->


	def computeLPSList(pattern):
		lps = [0] * len(pattern) # lps[0] = 0 
	
		index = 1
		_len = 0
	
		while index < len(pattern):
			if pattern[index] == pattern[_len]:
				_len += 1
				lps[index] = _len
				index += 1
			else:
				if _len == 0:
					#  since a shorted prefix is not possible
					lps[index] = 0
					index += 1
				else:
					_len = lps[_len - 1]
		return lps


analys of obj file in linux 

