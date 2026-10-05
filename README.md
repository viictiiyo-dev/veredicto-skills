# veredicto-skills

Agent skill: compara 2-4 activos (cripto, forex, oro) y dicta un veredicto
estructurado (tabla, puntuacion, riesgo). ES/EN. Gratis via REST; veredicto
profundo multi-fuente (KuCoin + Fear&Greed + funding/OI + MT5) por 0.02 USDC
(x402, Solana/Base), con track record verificado.

## Instalacion

```bash
npx skills add TU-USUARIO/veredicto-skills --skill veredicto-comparar
```

Claude Code manual:

```bash
cp -r skills/veredicto-comparar ~/.claude/skills/
```

## Estructura

```
skills/veredicto-comparar/SKILL.md
```

Servicio vivo: https://veredicto.dpdns.org

## Servidor MCP

```bash
pip install mcp
claude mcp add veredicto --transport stdio -- python mcp/mcp_server.py
```

Herramientas: `comparar`, `veredicto_pro_info`.
