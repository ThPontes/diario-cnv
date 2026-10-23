# Diário CNV

PWA pessoal para registrar tiques e acontecimentos com Comunicação Não-Violenta
(sentimento → necessidade → observação e pedido). Usuária: uma pessoa só, no Chrome do Android.
Interface e textos em português do Brasil.

## Estrutura
- `src/app.html` — **única fonte do app** (HTML, CSS e JS num arquivo, sem framework, sem build de JS).
- `build.py` — gera `index.html` a partir de `src/app.html` (divide no marcador `<!-- BODY -->`,
  acrescenta o head do PWA e troca o jsPDF do CDN pelo `vendor/`). Nunca edite `index.html` à mão.
- `sw.js` — service worker, cache para funcionar offline.
- `manifest.webmanifest`, `icons/` (`python3 icons/make_icons.py` regera os PNG).
- `vendor/jspdf.umd.min.js` — jsPDF 2.5.1, gera o PDF sem internet.

## Fluxo de mudança
1. Edite `src/app.html`.
2. `python3 build.py`.
3. Incremente `VERSION` em `sw.js` (senão o celular continua com a versão antiga em cache).
4. Commit de `src/app.html`, `index.html` e `sw.js` juntos e push na `main`.
   O GitHub Pages publica a `main` (raiz) em https://thpontes.github.io/diario-cnv/.

`src/app.html` também é publicado como link de teste (artifact do Claude). Lá o download e o
compartilhamento ficam bloqueados; o app trata isso com uma mensagem (`sandboxed`).

## Dados: não quebrar
- Tudo fica em `localStorage`, chave `diario-cnv-v1`, só no aparelho. Não há servidor nem conta.
  Não adicione backend, analytics ou qualquer envio de dados sem pedido explícito: é informação de saúde.
- Formato de cada registro (mantenha compatível; registros antigos precisam continuar abrindo):
  `{ id, when: "AAAA-MM-DDTHH:MM" (hora local), kind: "tique" | "evento", tic, obs,
     feelings: [string], intensity: 2|4|6|8|10 | null (exibido como 1–5), needs: [string], req }`
- Palavras são guardadas em minúsculas; palavras próprias (fora das listas) também ficam em `feelings`/`needs`.
- Não mude a chave do `localStorage` nem renomeie campos. Se for inevitável, migre os dados no carregamento.

## Conteúdo
- Listas de sentimentos e necessidades: Instituto CNV Brasil (PDFs fornecidos pelo usuário). Não invente palavras novas nas listas.
- Os agrupamentos por cor (Raiva, Medo e tensão, Tristeza, Cansaço / Paz, Alegria, Energia;
  Corpo, Segurança, Conexão, Autonomia, Sentido, Lazer) são nossos, não da fonte. A psicóloga pode pedir ajustes.
- As cores seguem convenções culturais das emoções. Não apresentar como terapêuticas.

## Testes
Sem suíte de testes. Para verificar, rode o `index.html` com Playwright
(Chromium em `/opt/pw-browsers/chromium`), preencha um registro e confira o relatório, o PDF (`pdfBlob()`)
e o CSV (`csvBlob()`). O erro de service worker em `file://` é esperado.
