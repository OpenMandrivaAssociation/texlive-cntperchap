%global tl_name cntperchap
%global tl_revision 37572

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Store counter values per chapter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cntperchap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cntperchap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cntperchap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package stores values of counters (which have been registered
beforehand) on a per chapter base and provides the values on demand in
the 2nd LaTeX compilation run. In this way it is possible to know how
many sections etc. there are lying ahead and to react to these counter
values, if needed. This is a preliminary version that has been tested
with book.cls, memoir.cls, and scrbook.cls. The packages assoccnt (by
the same author) and xparse are needed as well.

