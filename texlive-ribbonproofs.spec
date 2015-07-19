# revision 31137
# category Package
# catalog-ctan /macros/latex/contrib/ribbonproofs
# catalog-date 2013-07-08 10:43:32 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-ribbonproofs
Version:	1.0
Release:	9
Summary:	Drawing ribbon proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ribbonproofs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ribbonproofs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ribbonproofs.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
