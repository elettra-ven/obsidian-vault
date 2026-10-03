>[!note] Scope
>Moment in the execution where some name is available.

![[Pasted image 20261002112207.png|191]]
	1. Local
	2. Enclosing
	3. Global
	4. Built-in (**created when the interpreter starts up**)

>[!info] The `global` command
>It signals that a certain name should be taken/read from the global scope.

>[!info] The `nonlocal` command
>It signals that a certain name should be taken/read from the nonlocal (enclosing) scope.

`globals()` 
	returns the dict of the global names with their binding. 
	It can be modified.
`locals()` 
	returns the dict of the local names with their binding.

```
a = "global”

def f(): 
	a = "local to f"
	def g(): 
		a = "local to g"
		print(a) 
		def h(): 
			#nonlocal a 
			a = "local to h" 
			print(a) 
		h() 
		print(a) 
	g() 
f()
```