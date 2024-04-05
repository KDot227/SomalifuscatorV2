<h1 align="center">
  SomalifuscatorV2 (Batch is cool)
</h1>

<div align="center">
  <img  src="https://github.com/KDot227/SomalifuscatorV2/blob/main/assets/Eric%20Cartman%20Somalia.gif?raw=true">
  <br>
  <img  src="https://img.shields.io/github/languages/top/KDot227/SomalifuscatorV2?color=27c722">
  <img  src="https://img.shields.io/github/stars/KDot227/SomalifuscatorV2?color=27c722">
  <br>
  <img  src="https://img.shields.io/github/commit-activity/w/KDot227/SomalifuscatorV2?color=27c722">
  <img  src="https://img.shields.io/github/last-commit/KDot227/SomalifuscatorV2?color=27c722">
  <br>
  <img  src="https://img.shields.io/github/issues/KDot227/SomalifuscatorV2?color=27c722">
  <img  src="https://img.shields.io/github/issues-closed/KDot227/SomalifuscatorV2?color=27c722">
  <br>
  <hr  style="border-radius: 2%; margin-top: 60px; margin-bottom: 60px;"  noshade=""  size="20"  width="100%">
</div>

<h1 align="center">
  READ
</h1>

If you are AT&T or another major coporation please reach out to me I would like a job im poor.

<h2 align="center">
  How To Use
</h2>

Download python (any version past 3.10)\
Clone repo or download as zip (Then extract repo from zip (Yes people don't do that))\
Run setup.bat\
Have fun obfuscating!\
\
IMPORTANT\
When running somalifuscator for the first time you will have a .json file named settings. as you can guess these are your settings. If you are having any issues with scripts I recommend turning on debug mode (which will lower obfuscation levels) and trying to figure out the issue.\
\
If you have any issues please make a issue on github and I'll try to get to it as soon as possible.

<h1 align="center">
  Detections 😈
</h1>

Runtime test via scanner.to [results](https://scanner.to/result/9Vrtp48P58)

Scantime test via avcheck.net [results](https://avcheck.net/id/yfkokUq7WRIr)

Scantime test via Virustotal.com [results](https://www.virustotal.com/gui/file/589a7a6e7c45a94e2b8944a340cfe6dfc82068b9a30fce3160c827bf1a5aa437?nocache=1)

So far it's esentially fud when using the fud mode and only detected by 2 av when using the normal mode. Fud mode slightly brings down protection but I intend to fix that within the next update.\
\
Another interesting this is how Virus total currently thinks that the file is Javascript (It obviousily isn't)

<h1 align="center">
  But what if someone tries to deobfuscate 🤓
</h1>

Have fun and goodluck. If you end up making a full deobfuscator plz show me cause that's impressive

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
  Checks to make sure the first 3 bytes are UTF-16 BOM
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
  <summary>Bitwise Opperations (Xor, Not)</summary>
  XOR and NOT are both being used (I wish I could do MBA but batch sucks)
</details>
<details>
  <summary>Hot asf</summary>
  ngl from what I've seen, it's the best in the world and it'll probably stay that way
</details>

<h1 align="center">
  If you like this repo please give it a star ⭐
</h1>

<h3 align="center">
  Credits
</h3>

KDot227 (literally everything)\
Baum (Inspiration for the idea of the project)

Also @ John Hammond cause he's cool and I wanna see him deobfuscate this
