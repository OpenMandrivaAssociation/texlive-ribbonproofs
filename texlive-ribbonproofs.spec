%global tl_name ribbonproofs
%global tl_revision 31137

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Drawing ribbon proofs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ribbonproofs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ribbonproofs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ribbonproofs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a way to draw "ribbon proofs" in LaTeX. A ribbon
proof is a diagrammatic representation of a mathematical proof that a
computer program meets its specification. These diagrams are more human-
readable, more scalable, and more easily modified than the corresponding
textual proofs.

