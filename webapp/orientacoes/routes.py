from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from webapp import db
from webapp.models import Orientacao, User
from webapp.orientacoes.forms import OrientacaoForm

orientacoes = Blueprint('orientacoes', __name__)

@orientacoes.route("/minhasorientacoes")
def minhasorientacoes():
    page = request.args.get('page', 1, type=int)
    posts = Orientacao.query.order_by(Orientacao.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('minhasorientacoes.html', orientacoes=posts)

@orientacoes.route("/orientacao/new", methods=['GET', 'POST'])
@login_required
def new_orientacao():
    form = OrientacaoForm()
    if form.validate_on_submit():
        orientacao = Orientacao(pacname=form.pacname.data, paccpf=form.paccpf.data, content=form.content.data, author=current_user)
        db.session.add(orientacao)
        db.session.commit()
        flash('Your orientacao has been created!', 'success')
        return redirect(url_for('orientacoes.minhasorientacoes'))
    return render_template('create_orientacao.html', title='Nova Orientação',
                           form=form, legend='Nova Orientação')


@orientacoes.route("/orientacao/<int:orientacao_id>")
def orientacao(orientacao_id):
    orientacao = Orientacao.query.get_or_404(orientacao_id)
    return render_template('orientacao.html', pacname=orientacao.pacname, orientacao=orientacao)


@orientacoes.route("/orientacao/<int:orientacao_id>/update", methods=['GET', 'POST'])
@login_required
def update_orientacao(orientacao_id):
    orientacao = Orientacao.query.get_or_404(orientacao_id)
    if orientacao.author != current_user:
        abort(403)
    form = OrientacaoForm()
    if form.validate_on_submit():
        orientacao.pacname = form.pacname.data
        orientacao.paccpf = form.paccpf.data
        orientacao.content = form.content.data
        db.session.commit()
        flash('Sua orientacao foi atualizada!', 'successo')
        return redirect(url_for('orientacoes.minhasorientacoes', orientacao_id=orientacao.id))
    elif request.method == 'GET':
        form.pacname.data = orientacao.pacname
        form.paccpf.data = orientacao.paccpf
        form.content.data = orientacao.content
    return render_template('create_orientacao.html', title='Atualizar Orientação',
                           form=form, legend='Atualizar Orientação')


@orientacoes.route("/orientacao/<int:orientacao_id>/delete", methods=['POST'])
@login_required
def delete_orientacao(orientacao_id):
    orientacao = Orientacao.query.get_or_404(orientacao_id)
    if orientacao.author != current_user:
        abort(403)
    db.session.delete(orientacao)
    db.session.commit()
    flash('Your orientacao has been deleted!', 'success')
    return redirect(url_for('orientacoes.minhasorientacoes'))


@orientacoes.route("/orientacao/<string:username>")
def user_orientacoes(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    orientacoes = Orientacao.query.filter_by(author=user)\
        .order_by(Orientacao.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_orientacoes.html', orientacoes=orientacoes, user=user)