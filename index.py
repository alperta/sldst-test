import streamlit as st
import yaml
from yaml.loader import SafeLoader
import os

# Open the file and load the file
with open('data.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)

st.title('Souldust')

socials = data.get('social')
if socials:
	social_html = ''
	for social, social_url in socials.items():
		social_html += '<div style="display: inline; margin-right: 20px; width: 30px">'
		with open(f'svg-{social}', 'r') as svg_file:
			social_svg = svg_file.read()
		social_html += f'<a href="{social_url}">{social_svg}</a>'
		social_html += '</div>'
	st.markdown(social_html, unsafe_allow_html=True)


gigs = data.get('gigs')
if gigs:
	st.header('Upcoming Gigs')
	for gig, val in gigs.items():

		gig_date = gig
		gig_name = val.get('Name')
		gig_info = val.get('Info')

		gig_html = f'<div style="background: #EEE; padding: 3px 20px 10px; margin-bottom: 20px; border-radius: 5px; border: 1px solid #DDD"><h3>{gig_date} - {gig_name}</h3>'

		if gig_info:
			gig_html += f'<p>{gig_info}</p>'
		gig_url = val.get('URL')
		
		if gig_url:
			gig_html += f'<a href="{gig_url}">More info</a>'

		st.markdown(gig_html, unsafe_allow_html=True)

musics = data.get('music')
if musics:
	st.header('Music')
	for track in musics:
		st.markdown(f'<iframe width="100%" height="300" style="margin-bottom: 20px" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url={track}&color=%23ff5500&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false&visual=false"></iframe>', unsafe_allow_html=True)