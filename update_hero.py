from pathlib import Path
p = Path('/home/ubuntu/ana-trufas-delivery/client/src/pages/Home.tsx')
s = p.read_text()
start = s.index('        <section id="inicio"')
end = s.index('        <section id="cardapio"', start)
hero = '''        <section id="inicio" className="relative min-h-[680px] overflow-hidden bg-[#f7e6e9]">
          <img src="/manus-storage/ana-trufas-dona_cf0017e6.webp" alt="Ana, fundadora da Ana Trufas, preparando doces" className="absolute inset-0 h-full w-full object-cover object-[66%_center] sm:object-center" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#fffaf7]/98 via-[#fffaf7]/90 via-45% to-[#fffaf7]/5" />
          <div className="absolute inset-0 bg-gradient-to-t from-[#6e203a]/10 via-transparent to-white/10" />
          <div className="relative mx-auto flex min-h-[680px] max-w-7xl items-center px-5 py-16 lg:px-10">
            <div className="max-w-xl rounded-[32px] border border-white/70 bg-[#fffaf7]/72 p-6 shadow-[0_24px_70px_rgba(110,32,58,.10)] backdrop-blur-sm sm:p-9">
              <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-[#e5afbf] bg-white/75 px-3 py-2 text-[11px] font-bold uppercase tracking-[.18em] text-[#8f294c]"><Sparkles size={14} /> delivery em Maceió · todos os dias</div>
              <h1 className="font-display text-5xl font-bold leading-[.98] tracking-[-.045em] text-[#6e203a] sm:text-6xl">Seu doce favorito, <em className="font-serif font-normal text-[#ba5274]">a caminho.</em></h1>
              <p className="mt-6 max-w-md text-lg leading-relaxed text-[#795b60]">Bolos, doces, kits festa e salgados feitos com carinho — você pede pelo site e a Ana confirma tudo pelo WhatsApp.</p>
              <div className="mt-8 flex flex-wrap items-center gap-3"><a href="#cardapio" className="inline-flex h-12 items-center gap-2 rounded-full bg-[#8f294c] px-6 text-sm font-bold text-white shadow-[0_14px_30px_rgba(143,41,76,.22)] transition hover:-translate-y-1">Pedir agora <ArrowRight size={17} /></a><a href="https://wa.me/5582994003462" target="_blank" rel="noreferrer" className="inline-flex h-12 items-center gap-2 rounded-full border border-[#dca6b6] bg-white/75 px-5 text-sm font-bold text-[#8f294c] transition hover:bg-white">Tirar dúvidas</a></div>
              <div className="mt-9 grid max-w-md grid-cols-3 gap-3 border-t border-[#e8ced3] pt-6"><div><p className="text-xs font-bold uppercase tracking-[.1em] text-[#8f294c]">1º passo</p><p className="mt-1 text-xs text-[#806166]">Escolha seus favoritos</p></div><div><p className="text-xs font-bold uppercase tracking-[.1em] text-[#8f294c]">2º passo</p><p className="mt-1 text-xs text-[#806166]">Monte a sacola</p></div><div><p className="text-xs font-bold uppercase tracking-[.1em] text-[#8f294c]">3º passo</p><p className="mt-1 text-xs text-[#806166]">Finalize no WhatsApp</p></div></div>
            </div>
          </div>
        </section>

'''
s = s[:start] + hero + s[end:]
s = s.replace('para adoçar o seu dia', 'peça pelo delivery')
s = s.replace('Escolha o seu favorito', 'Monte seu pedido')
s = s.replace('Tudo feito sob encomenda, com ingredientes selecionados e aquele toque especial da Ana.', 'Escolha seus favoritos, adicione à sacola e envie o pedido. A Ana confirma disponibilidade, taxa e prazo pelo WhatsApp.')
s = s.replace('um carinho que começou em casa', 'feito por quem ama o que faz')
s = s.replace('“Cada encomenda leva um pedacinho da nossa história.”', '“Você pede daí. A gente prepara daqui. E o carinho chega junto.”')
s = s.replace('Celebrar é melhor quando tem afeto.', 'Do nosso forno para a sua celebração.')
p.write_text(s)
print('hero updated')
