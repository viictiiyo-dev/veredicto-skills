#!/usr/bin/env python3
"""Veredicto como servidor MCP (stdio). Expone comparar gratis + info pro/track.

Uso Claude Desktop / Code / Cursor:
  claude mcp add veredicto --transport stdio -- \
    "C:\\Program Files\\Python311\\python.exe" src/mcp_server.py
"""
import json
import urllib.request

from mcp.server.mcpserver import MCPServer

BASE = "https://veredicto.dpdns.org"

mcp = MCPServer("veredicto")


def _get(path: str) -> dict:
    req = urllib.request.Request(
        BASE + path, headers={"User-Agent": "veredicto-mcp/0.1", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


@mcp.tool()
def comparar(monedas: str) -> str:
    """Compara 2-4 criptomonedas y devuelve ganador con tabla. Gratis.
    monedas: lista separada por comas de btc, eth, sol, bnb, xrp, doge, ada, avax.
    Ej: 'btc,eth,sol'. ES/EN. No es asesoramiento financiero."""
    syms = [s.strip().lower() for s in monedas.split(",") if s.strip()][:4]
    d = _get("/comparar?monedas=" + ",".join(syms))
    v = d["veredicto"]
    lines = [f"Veredicto: gana {v['winner']}."]
    for r in v["table"]:
        lines.append(
            f"- {r['symbol']}: {r['price']} USD | 24h {r['change_24h']}% | "
            f"riesgo {r['risk']} | score {r['score']}")
    lines.append(v["note"])
    return "\n".join(lines)


@mcp.tool()
def veredicto_pro_info() -> str:
    """Precio, metodos de pago x402 y track record del veredicto profundo.
    El pro multi-fuente (precio+sentimiento+funding, confianza 0-100) cuesta
    0.02 USDC en Solana o Base via POST /comparar/pro con PAYMENT-SIGNATURE."""
    pro = _get("/comparar/pro")
    t = _get("/track")
    nets = ", ".join(f"{m['network']} -> {m['payTo']}" for m in pro["methods"])
    return (f"Precio: {pro['price']}. Redes: {nets}. "
            f"Track: {t['hits']}/{t['total']} aciertos "
            f"({t['hit_rate']}) + {t['pendientes']} pendientes. {pro['how']}")


if __name__ == "__main__":
    mcp.run()
