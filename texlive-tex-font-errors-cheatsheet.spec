# revision 18314
# category Package
# catalog-ctan /info/tex-font-errors-cheatsheet
# catalog-date 2010-05-16 21:06:03 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tex-font-errors-cheatsheet
Version:	0.1
Release:	1
Summary:	Cheat sheet outlining the most common TeX font errors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/tex-font-errors-cheatsheet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-font-errors-cheatsheet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-font-errors-cheatsheet.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a compact three-pages document highlighting the TeX
flow of integrating fonts, and explains how some of the most
common font-related error messages occur. Also, hints are given
on how to address those.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tex-font-errors-cheatsheet/README
%doc %{_texmfdistdir}/doc/latex/tex-font-errors-cheatsheet/tex-font-cheatsheet.pdf
%doc %{_texmfdistdir}/doc/latex/tex-font-errors-cheatsheet/tex-font-cheatsheet.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
