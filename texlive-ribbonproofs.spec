Name:		texlive-ribbonproofs
Version:	31137
Release:	1
Summary:	Drawing ribbon proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ribbonproofs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ribbonproofs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ribbonproofs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a way to draw "ribbon proofs" in LaTeX. A
ribbon proof is a diagrammatic representation of a mathematical
proof that a computer program meets its specification. These
diagrams are more human-readable, more scalable, and more
easily modified than the corresponding textual proofs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ribbonproofs/ribbonproofs.sty
%doc %{_texmfdistdir}/doc/latex/ribbonproofs/README
%doc %{_texmfdistdir}/doc/latex/ribbonproofs/ribbonproofsmanual.pdf
%doc %{_texmfdistdir}/doc/latex/ribbonproofs/ribbonproofsmanual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
