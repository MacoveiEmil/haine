<#
  Planificator recrawl hainute.ro (Windows Task Scheduler).
  Moduri:
    daily  — reîmprospătează tot catalogul (Answear + Fashion Days), rulat de 2x/zi.
    hot    — doar produsele fierbinți (multe vizualizări recente), rulat orar.

  Exemplu manual:  powershell -File cron.ps1 -Mode daily
  Env opțional: SITE, SECRET, MAX.
#>
param([ValidateSet('daily','hot')][string]$Mode = 'daily')

$ErrorActionPreference = 'Stop'
Set-Location -Path $PSScriptRoot
$log = Join-Path $PSScriptRoot ("refresh-{0}.log" -f $Mode)
"`n===== $(Get-Date -Format 'yyyy-MM-dd HH:mm')  mod=$Mode =====" | Add-Content $log

if ($Mode -eq 'hot') {
  # Lane rapid: puține produse, ambele surse, ca stocul celor populare să fie proaspăt.
  node refresh.js cj hot *>> $log
  node refresh.js fd hot *>> $log
} else {
  # Rulare completă: se auto-plafonează la MAX (implicit 1200/sursă); rulată de
  # 2x/zi acoperă catalogul în câteva runde, cele mai vechi verificate întâi.
  node refresh.js cj *>> $log
  node refresh.js fd *>> $log
}
# Lane CROSS: URL-urile de pe alte magazine (Zalando, epantofi, Modivo, AboutYou,
# Fashion Days, Sportisimo...) — preț, stoc și mărimi per magazin. ~900 de URL-uri,
# deci doar în modul daily și doar cele neverificate de 10h (OLDER) → fiecare URL
# e re-verificat de ~2x/zi. Magazinele merg în paralel, fiecare vizitat încet.
if ($Mode -eq 'daily') {
  $env:OLDER = '10'
  node manual.js *>> $log
}
# La final: recalculează „are stoc" + prețul minim pe tot catalogul (ordinea din
# listări: produsele disponibile primele). Unele crawlere scriu stocul direct în tabel.
$site = if ($env:SITE) { $env:SITE } else { 'http://hainutero.local' }
try { Invoke-RestMethod "$site/wp-json/hainute/v1/recompute-buyable?secret=$($env:SECRET)" | Out-String | Add-Content $log } catch { "recompute-buyable: $_" | Add-Content $log }
"gata $(Get-Date -Format 'HH:mm')" | Add-Content $log
