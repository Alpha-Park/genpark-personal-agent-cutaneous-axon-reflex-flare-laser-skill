"""
MCP Server for Cutaneous Axon Reflex Flare Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating Laser Doppler flare flux, Vasodilatory Index, and C-fiber scores.
"""

import sys
import json
from typing import Dict, Any
from client import CutaneousAxonReflexFlareClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_axon_reflex_flare",
                "description": "Calculates Cutaneous Axon Reflex Vasodilatory Index (PU_peak/PU_base), flare radius (mm), and unmyelinated C-fiber axonal integrity score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_flux_pu": {
                            "type": "number",
                            "description": "Baseline cutaneous perfusion units via Laser Doppler (e.g. 15.0 PU)."
                        },
                        "peak_flare_flux_pu": {
                            "type": "number",
                            "description": "Peak flare cutaneous perfusion units after stimulation (e.g. 85.0 PU)."
                        },
                        "flare_radius_mm": {
                            "type": "number",
                            "description": "Radius of cutaneous neurogenic erythema/flare in millimeters (e.g. 18.0 mm, normative 12-25 mm)."
                        },
                        "stimulus_type": {
                            "type": "string",
                            "description": "Nociceptive axon reflex trigger method (default: HISTAMINE_IONTOPHORESIS).",
                            "default": "HISTAMINE_IONTOPHORESIS"
                        }
                    },
                    "required": ["baseline_flux_pu", "peak_flare_flux_pu", "flare_radius_mm"]
                }
            }
        ]
    }


def handle_request(client: CutaneousAxonReflexFlareClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_axon_reflex_flare":
            res = client.evaluate_axon_reflex_flare(
                baseline_flux_pu=float(args.get("baseline_flux_pu", 15.0)),
                peak_flare_flux_pu=float(args.get("peak_flare_flux_pu", 85.0)),
                flare_radius_mm=float(args.get("flare_radius_mm", 18.0)),
                stimulus_type=str(args.get("stimulus_type", "HISTAMINE_IONTOPHORESIS"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CutaneousAxonReflexFlareClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
