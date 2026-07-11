%global tl_name tex-font-errors-cheatsheet
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Cheat sheet outlining the most common TeX font errors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-font-errors-cheatsheet
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-font-errors-cheatsheet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-font-errors-cheatsheet.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a compact three-pages document highlighting the TeX flow of
integrating fonts, and explains how some of the most common font-related
error messages occur. Also, hints are given on how to address those.

