Name:		texlive-cntperchap
Version:	37572
Release:	2
Summary:	Store counter values per chapter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cntperchap
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cntperchap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cntperchap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package stores values of counters (which have been
registered beforehand) on a per chapter base and provides the
values on demand in the 2nd LaTeX compilation run. In this way
it is possible to know how many sections etc. there are lying
ahead and to react to these counter values, if needed. This is
a preliminary version that has been tested with book.cls,
memoir.cls, and scrbook.cls. The packages assoccnt (by the same
author) and xparse are needed as well.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cntperchap
%doc %{_texmfdistdir}/doc/latex/cntperchap

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
