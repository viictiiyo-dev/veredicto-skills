---
name: veredicto-comparar
description: Compara 2-4 activos (cripto, forex, oro) y devuelve un ganador con tabla, riesgo y puntuacion. Gratis via REST; veredicto profundo multi-fuente por 0.02 USDC (x402, Solana/Base). ES/EN.
---

# Veredicto - Comparador Cripto, Forex y Oro

Compara activos y dicta un ganador estructurado. Sin clave ni cuenta.

## Tier gratis (REST)

```
GET https://veredicto.dpdns.org/comparar?monedas=btc,eth,sol
GET https://veredicto.dpdns.org/comparar?monedas=eurusd,gbpusd
```

- `monedas`: 2-4 de `btc, eth, sol, bnb, xrp, doge, ada, avax, eurusd, gbpusd, usdjpy, xauusd`.
- Responde `{veredicto: {winner, note, table: [{symbol, price, change_24h, risk, score}]}}`.
- `score` ordena de mejor a peor; `winner` es el primero.

Ejemplos de uso:

- Usuario: "compara btc vs eth" -> `GET .../comparar?monedas=btc,eth`, presenta ganador + tabla.
- Usuario: "sol, ada o xrp, cual va mejor" -> `GET .../comparar?monedas=sol,ada,xrp`.
- Usuario: "euro o libra" -> `GET .../comparar?monedas=eurusd,gbpusd`.
- Usuario: "oro vs bitcoin" -> `GET .../comparar?monedas=xauusd,btc`.

## Tier pro ($0.02 USDC, x402)

Veredicto profundo multi-fuente (precio/volumen KuCoin triangulado con
BingX, sentimiento Fear&Greed, funding y su tendencia, open interest, basis
mark/indice, flujo DEX onchain (GeckoTerminal + DEX Screener de repuesto),
ticks MT5 con spread real en forex/oro) con confianza 0-100
y track record verificado a 7 dias:

```
GET https://veredicto.dpdns.org/comparar/pro   -> 402 con precio, metodos y extension Bazaar
GET https://veredicto.dpdns.org/track          -> hits, total, hit_rate
POST https://veredicto.dpdns.org/comparar/pro {"opciones":["btc","eth"]}
  Header: PAYMENT-SIGNATURE: <payload x402 en base64>
```

Sin firma responde 402 con el reto en el header `PAYMENT-REQUIRED`.
Redes: Solana y Base, esquema `exact`, 20000 unidades (0.02 USDC).
Destinos: Solana `9F2PzCVPZ7V7WATG732WH4sf31gSXiHKyx3UmdSDvFQo`,
Base `0x139a680FCa575cfA5ADA25b5417fe9fDeE8ED06E`.

## Reglas

- Responde siempre en el idioma del usuario (ES/EN).
- Nunca es asesoramiento financiero: incluye el `note` tal cual.
- Si el usuario pide "profundo/premium/pro", usa el tier pro y explica el pago.
