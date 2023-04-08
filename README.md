<h1 align="center">
  Somalifuscator (Batch is cool)
</h1>

<div align="center">
  <img  src="https://github.com/KDot227/Somalifuscator/blob/main/assets/Eric%20Cartman%20Somalia.gif?raw=true">
  <br>
  <img  src="https://img.shields.io/github/languages/top/KDot227/Somalifuscator?color=27c722">
  <img  src="https://img.shields.io/github/stars/KDot227/Somalifuscator?color=27c722">
  <br>
  <img  src="https://img.shields.io/github/commit-activity/w/KDot227/Somalifuscator?color=27c722">
  <img  src="https://img.shields.io/github/last-commit/KDot227/Somalifuscator?color=27c722">
  <br>
  <img  src="https://img.shields.io/github/issues/KDot227/Somalifuscator?color=27c722">
  <img  src="https://img.shields.io/github/issues-closed/KDot227/Somalifuscator?color=27c722">
  <br>
  <img  src="https://shields-io-visitor-counter.herokuapp.com/badge?page=KDot227.Somalifuscator&color=27c722">
  <hr  style="border-radius: 2%; margin-top: 60px; margin-bottom: 60px;"  noshade=""  size="20"  width="100%">
</div>

<h1 align="center">
  READ
</h1>

<h2 align="center">
  How To Use
</h2>

Download python (any version past 3.10)\
Clone repo or download as zip (Then extract repo from zip (Yes people don't do that))\
Run setup.bat\
Have fun obfuscating!

Note: You can use the gui version if you want but it's missing a lot of features that the normal version has.

<h1 align="center">
  But what if someone tries to deobfuscate 🤓
</h1>

Here are a couple of cool things Somalifuscator (ultimate mode) does to make it harder to deobfuscate:
* File can't be opened in notepad or notepad ++
* When you use something such as [this](https://github.com/DissectMalware/batch_deobfuscator) it can't get past this first layer. If you give it a chance and take that layer off it can't even interpret the code because of all the unicode. ON TOP OF THAT even if you have all other settings disabled it STILL won't be able to deobfuscate all the way. This is why Somalifuscator is the best batch obfuscator to ever be made.
* In the end I'm not saying it's impossible to deobfuscate since technically every obfuscation is deobfuscateable. I'm just saying that this obfuscation is the best chance you have to prevent the inevitable deobfuscation

<h1 align="center">
  Features
</h1>

<details>
  <summary>Anti VM</summary>
  Literially checks if the current computer is a VM and if it is it exits
</details>
<details>
  <summary>Anti Echo</summary>
  Looks for any variation of the word ECHO. If it's found it exits. Also some of the other settings make it very very hard to echo commands and understand output
</details>
<details>
  <summary>Anti Byte Change</summary>
  Checks to make sure the first 3 bytes are obfuscated asf
</details>
<details>
  <summary>Environment variable obfuscation</summary>
  Uses built in Windows Environment Variables to help obfuscate code
</details>
<details>
  <summary>Built in var support</summary>
  I went through the dedication to list out nearly every built in var + make a regex that can find them all for multiple instances.
</details>
<details>
  <summary>Errorlevel continuation</summary>
  Using errorlevel won't break the code since using goto and labels dont establish an error level unless the label can't be found (which it always should be able to be found)
</details>
<details>
  <summary>Hot asf</summary>
  ngl from what I've seen, it's the best in the world and hopefully it stays that way
</details>

<h2 align="center">
  Why make this?
</h2>

Long story short baum made [this](https://github.com/baum1810/batchobfuscator) and I thought that it was cool and thought that I could also make something better and so I did. I left it alone after making the first 3 modes but then picked it up again after some kid said that his was better.

<h2 align="center">
  Cool Things
</h2>

Not only is the Obfuscator very fast but it's also very customizable. If you know python code well enough nothing is stopping you from going into the code and changing some of the randint values to occur more frequently making your code more obfuscated and harder to read.

<h2 align="center">
  Cool map thing I drew
</h2>

![map](https://i.imgur.com/Lc0EAe0.png)

<h2 align="center">
  Level 1
</h2>

![level 1](https://i.imgur.com/g6XpRIj.png)

<h2 align="center">
  Level 2
</h2>

![level 2](https://i.imgur.com/aQQe5wE.png)

<h2 align="center">
  Level 3
</h2>

![level 3](https://i.imgur.com/nVsqpmm.png)

<h2 align="center">
  Level 4 (edited by me to actually work :skull:))
</h2>

No image provided

<h2 align="center">
  Level 5 (not made by me))
</h2>

No image provided

<h2 align="center">
  Fud Mode (Undetected from virus total)
</h2>

![fud mode (undetected from virus total)](https://i.imgur.com/0gy7szh.png)

<h2 align="center">
  All (applies 1, 2 and 3) NOTE THIS IS OUTDATED USE ULTIMATE
</h2>

![all levels (looks the same as level 3 but has levels 2 and 1 also applied)](https://i.imgur.com/g2vvIwo.jpeg)

<h2 align="center">
  The "Ultimate" Batch Obfuscation (You can't open it in notepad or notepad++ or else it crashes)
</h2>

![Ultimate Mode](https://i.imgur.com/flte4s3.jpeg)

<h2 align="center">
  Embed
</h2>

No image but it embeds powershell files (ps1 files) at the end of the batch script and when ran the batch script will rerun with powershell which runs the powershell. (I will eventually add Jscript/Wscript and maybe full support for Vbs)

<h1 align="center">
  If you like this repo please give it a star ⭐
</h1>

Also @ John Hammond cause he's cool and I wanna see him deobfuscate this
