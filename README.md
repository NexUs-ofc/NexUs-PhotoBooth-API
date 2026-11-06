# NexUs PhotoBooth API

API FastAPI do PhotoBooth Expotech. O app mobile envia a foto final em JPEG; o backend valida os dados e solicita o envio da imagem com legenda à instância GREEN-API configurada no servidor.

## Configuração

Requer Python 3.10+.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Preencha `.env` com os parâmetros da instância no painel GREEN-API (`GREENAPI_API_URL`, `GREENAPI_MEDIA_URL`, `GREENAPI_ID_INSTANCE`, `GREENAPI_API_TOKEN_INSTANCE`) e gere uma chave longa para `PHOTOBOOTH_API_KEY`. Mantenha o token GREEN-API só no servidor. Autorize o WhatsApp nessa instância pelo QR do painel.

Configure o app com `EXPO_PUBLIC_PHOTOBOOTH_API_URL` apontando para a URL HTTPS pública desta API e `EXPO_PUBLIC_PHOTOBOOTH_API_KEY` igual à chave `PHOTOBOOTH_API_KEY`.

## Executar

```powershell
uvicorn app.main:app --reload
```

Documentação interativa: `http://127.0.0.1:8000/docs`. Healthcheck: `GET /health`.

## Endpoints

- `GET /photobooth/status` — requer `X-PhotoBooth-Key`; retorna o estado da instância sem expor credenciais.
- `POST /photobooth/send` — requer multipart/form-data com `name`, `phone`, `consent=true` e `photo` (JPEG), além de `X-PhotoBooth-Key`.

A API normaliza telefones brasileiros para DDI 55, limita o upload (10 MB por padrão; máximo configurável de 20 MB), valida consentimento e assinatura JPEG e só envia quando a instância estiver `authorized`. Usa GREEN-API `sendFileByUpload`, com a legenda `Obrigado por visitar nosso stand {nome}!💜`. Resposta `202` e `idMessage` significam que a mídia entrou na fila, não confirmam entrega no WhatsApp.

## Testes

```powershell
python -m unittest discover -s tests -v
```

Os testes usam transporte HTTP simulado; não fazem chamadas reais à GREEN-API.
