>[!info] Il DNA è una **struttura topologicamente definita**: non ha estremità libere di ruotare

- DNA **batterico**:
	Struttura circolare.
	Il numero di volte che un filamento gira attorno all'altro NON può cambiare.
- DNA **eucariotico**:
	Struttura lineare.
	È legato a proteine vincolanti e organizzato in cromatina.

Quando la doppia elica viene aperta e le estremità **non possono ruotare**, si formano **==superavvolgimenti==** (se non ce ne sono il DNA si dice *rilassato*).

>[!tip] Linking number
>$$L_k = T_w + W_r$$
>- $L_k$ **numero di legame**:
>	Numero totale di volte che un filamento passa intorno all'altro.
>- $T_w$ **twist**:
>	Giri dell'elica ($\sim 25$ nella struttura rilassata).
>- $W_r$ **writhe**:
>	Numero di volte che la doppia elica si incrocia con sé stessa in un altro punto.
>	**Indica i superavvolgimenti**.

## Superavvolgimento negativo e apertura locale

Fisiologicamente, il DNA è superavvolto negativamente, con punti deboli di apertura locale che facilitano gli enzimi nell'apertura dell'elica.

La presenza di aperture locali è una proprietà in equilibrio con il superavvolgimento negativo (sono detti **[[#Topoisomerasi|topoisomeri]]**, ovvero con stesso $L_k$).
Anche i **nucleosomi** impongono superavvolgimenti negativi.

La presenza di superavvolgimenti positivi, invece, rende l'apertura più difficile.
(Questo comportamento è tipico di **estremofili**, come *Thermus aquaticus*)

## Topoisomerasi

**L'unico modo di cambiare $L_k$ è tagliare** uno o due filamenti. 
Durante la replicazione, i superavvolgimenti alle estremità iniziano a diventare sempre più “folti” non essendo liberi di ruotare; ciò potrebbe essere un problema per la forca replicativa se non ci fossero degli enzimi deputati a “rilassare” il DNA: 
	==le topoisomerasi rimuovono proprio questi superavvolgimenti. ==
Sono vitali.

Introducono una rottura del singolo o del doppio filamento in modo temporaneo.


|              | **Topoisomerasi I** | **Topoisomerasi II**     |
| ------------ | ------------------- | ------------------------ |
| Taglio       | **un** filamento    | **entrambi** i filamenti |
| $\Delta L_k$ | 1                   | 2                        |
>[!Abstract] **Meccanismo (senza ATP né cofattori ad alta energia):**
>
>1. Una **tirosina** del sito catalitico attacca un legame fosfodiesterico del DNA.
>2. Il DNA si rompe e l'enzima resta legato **covalentemente** a un'estremità con un **legame fosfotirosinico**.
>   L'altra estremità ($3'-OH$) è tenuta saldamente.
>3. Il legame fosfotirosinico **conserva l'energia** del legame fosfodiesterico idrolizzato.
>4. L'altro filamento (o doppia elica) passa attraverso la rottura.
>5. Il $3'-OH$ attacca il legame fosfotirosinico.
>   Di conseguenza, si rigenera il legame fosfodiesterico, l'enzima si libera.

---
## Elettroforesi su gel di agarosio
Essendo il DNA caricato negativamente, quando sottoposto ad un campo elettrico, questo migra verso il polo positivo, attraversando la matrice di agarosio.

A parità di campo, i frammenti più piccoli "corrono" più veloci, mentre quelli più grandi vengono rallentati.

Per un DNA circolare (**plasmide**) si osservano 3 forme:
1. **superavvolto**, il più veloce.
2. **lineare**, di velocità intermedia.
3. **circolare rilassato**, il più lento.

>[!abstract] Visualizzare il DNA
>Per visualizzare il DNA, che normalmente sarebbe invisibile, si usa il ==**bromuro di etidio**==, molecola planare che si **intercala** nella doppia elica, assorbe UV ed emette nel visibile (solo quando intercalato).
>
>Il gel su un transilluminatore UV mostra le bande di sedimentazione.

>[!warning] Conclusioni
>Il DNA è superavvolto (per apertura dell'elica o perché legato a proteine/cromatina). 
>Di solito questo avvolgimento avviene in modo negativo, il che lo mantiene in equilibrio con una forma localmente denaturata e aiuta ad aprire la bolla di replicazione. 
>
>Il $L_k$ dipende da $T_w + W_r$. 
>Solo tagliando uno o due filamenti si rimuovono i superavvolgimenti: lo fanno le **topoisomerasi**.
