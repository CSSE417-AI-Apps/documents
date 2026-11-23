"""Regenerate the highlighted variants of phase0_stages.svg (run from Slides/images)."""
import re
src = open('phase0_stages.svg').read()
CX = [125, 375, 625, 875, 1125, 1375]
variants = {
    'phase0_stage1_discovery': [1], 'phase0_stage2_download': [2], 'phase0_stage3_transcripts': [3],
    'phase0_stage4_chunks': [4], 'phase0_stage5_embeddings': [5], 'phase0_stage6_search': [6],
    'phase0_part1_data': [1, 2, 3], 'phase0_part2_vectors': [4, 5, 6],
}
for name, stages in variants.items():
    c0, c1 = CX[stages[0] - 1], CX[stages[-1] - 1]
    s = src.replace('</defs>', f'''</defs>

  <!-- highlight -->
  <rect x="{c0-112}" y="10" width="{c1-c0+224}" height="286" rx="22" fill="#FFF4EF" stroke="#E8572A" stroke-width="3" stroke-dasharray="10 8"/>''', 1)
    for n in stages:
        s = re.sub(rf'<text x="{CX[n-1]}"(\s+)y="(\d+)"( fill="[^"]*")?>', rf'<text x="{CX[n-1]}"\1y="\2" fill="#E8572A">', s)
    open(name + '.svg', 'w').write(s)
    print(name)
