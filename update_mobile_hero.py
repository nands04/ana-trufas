from pathlib import Path
p = Path('/home/ubuntu/ana-trufas-delivery/client/src/pages/Home.tsx')
s = p.read_text()
s = s.replace('className="absolute inset-0 h-full w-full object-cover object-[66%_center] sm:object-center"', 'className="absolute inset-0 hidden h-full w-full object-cover object-[66%_center] sm:block sm:object-center"')
s = s.replace('className="relative min-h-[680px] overflow-hidden bg-[#f7e6e9]"', 'className="relative min-h-0 overflow-hidden bg-[#f7e6e9] sm:min-h-[680px]"')
s = s.replace('''          <div className="absolute inset-0 bg-gradient-to-t from-[#6e203a]/10 via-transparent to-white/10" />
          <div className="relative mx-auto flex min-h-[680px] max-w-7xl items-center px-5 py-16 lg:px-10">''', '''          <div className="absolute inset-0 bg-gradient-to-t from-[#6e203a]/10 via-transparent to-white/10" />
          <div className="relative mx-auto w-full max-w-7xl px-5 pt-7 sm:hidden">
            <img src="/manus-storage/ana-trufas-dona_cf0017e6.webp" alt="Ana, fundadora da Ana Trufas, preparando doces" className="h-56 w-full rounded-[28px] object-cover object-[66%_center] shadow-[0_18px_40px_rgba(110,32,58,.14)]" />
          </div>
          <div className="relative mx-auto flex min-h-0 max-w-7xl items-center px-5 py-10 sm:min-h-[680px] sm:py-16 lg:px-10">''')
p.write_text(s)
print('responsive hero updated')
